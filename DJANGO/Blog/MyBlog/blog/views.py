from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, FormView
from .models import Post, Comment, Tag
from django.db.models import Q
from .forms import PostForm, PostShare, CommentForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import UserIsAuthorMixin
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.messages import success
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


# Create your views here.

class PostListView(ListView):
  template_name = 'post_list.html'
  queryset = Post.published.all()
  context_object_name = 'posts'
  paginate_by = 5

  def get_context_data(self, *args, **kwargs):
    
    data = super(PostListView, self).get_context_data(*args, **kwargs)
    search_filter =  self.request.GET.get('q')
    if search_filter: 
      data['posts'] = Post.published.search(search_filter)
    return data

class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  template_name = 'post_form.html'
  model = Post
  form_class = PostForm
  success_message = "%(title)s created successfully!"


  def form_valid(self, form):
    tags = form.cleaned_data.get('tags').split(',')
    
    # print("form.cleaned_data.get('tags')", form.cleaned_data.get('tags'))
    instance = form.save(commit=False)
    instance.author = self.request.user
    instance = form.save()
    for tag in tags:
      tag, created = Tag.objects.get_or_create(tag=tag)
      instance.tag.add(tag)
    #instance.save()
    return super(PostCreateView, self).form_valid(form)
    # print(form)
    # return form
  
class PostDetailView(DetailView, FormView):
  model = Post
  template_name = 'post_detail.html'
  form_class = CommentForm
  paginate_by = 1

  def form_valid(self, form):
    instance = form.save(commit=False)
    instance.post = self.get_object()
    instance.save()
    return super(PostDetailView, self).form_valid(form)
  
  def get_success_url(self):
    return reverse('post:detail', kwargs={'slug':self.get_object().slug})
  
  def get_context_data(self, **kwargs):
    context = super(PostDetailView, self).get_context_data( **kwargs)
    post = self.get_object()
    context['comments'] = post.get_comments() #Comment.actives.all()
    paginator = Paginator(context['comments'], 3) # Show 1 contacts per page.

    page_number = self.request.GET.get('page')
    context['page_obj'] = paginator.get_page(page_number)
    # print(context)
    return context

class PostUpdateView(UserIsAuthorMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  model = Post
  template_name = 'post_form.html'
  fields = ['title', 'status', 'body']
  success_message = "%(title)s updated successfully"

def share_post(request, slug):
  post = get_object_or_404(Post, slug=slug)
  form = PostShare(request.POST or None)
  if request.POST:
    if form.is_valid():
      name = form.cleaned_data.get('name')
      your_email = form.cleaned_data.get('your_email')
      friend_email = form.cleaned_data.get('friend_email')
      url = request.build_absolute_uri(reverse('post:detail', kwargs={'slug': post.slug}))
      subject = 'Your friend {} share {} with you'.format(name, post.title)
      message = 'Hello Please have a look on {} regards {} contact {}'.format(url, name, your_email)
      
      send_mail(subject, message, 'contact.findus@gmail.com',[friend_email])
      success(request, 'Mail sent successfully!')
      return HttpResponseRedirect(reverse('post:detail', kwargs={'slug': post.slug}))
  context = {'form':form, 'post':post}
  return render(request, 'share.html', context)

class SharePostView(SuccessMessageMixin, DetailView, FormView):
  model = Post
  template_name = 'share.html'
  form_class = PostShare
  success_message = 'Mail sent successfully!'
  

  def form_valid(self, form):
    post = self.get_object()
    name = form.cleaned_data.get('name')
    your_email = form.cleaned_data.get('your_email')
    friend_email = form.cleaned_data.get('friend_email')
    url = self.request.build_absolute_uri(reverse('post:detail', kwargs={'slug': post.slug}))
    subject = 'Your friend {} share {} with you'.format(name, post.title)
    message = 'Hello Please have a look on {} regards {} contact {}'.format(url, name, your_email)
    
    send_mail(subject, message, 'contact.findus@gmail.com',[friend_email])
    return super(SharePostView, self).form_valid(form)

  def get_success_url(self):
    post = self.get_object()
    return reverse('post:detail', kwargs={'slug':post.slug})

class GetPostByTags(ListView):
  template_name = 'post_list.html'
  context_object_name = 'posts'
  paginate_by = 5

  def get_queryset(self):
    tag = self.request.GET.get('tag')
    return Post.objects.filter(tag__tag=tag)

  def get_context_data(self, *args, **kwargs):
    context = super(GetPostByTags, self).get_context_data(*args, **kwargs)
    print(context)
    return context