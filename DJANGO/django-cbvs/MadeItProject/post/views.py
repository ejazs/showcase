from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.urls import reverse_lazy
from .forms import CommentForm
from django.http import HttpResponseRedirect
# Create your views here.

class PostListView(ListView):
  model = Post
  template_name = 'post_list.html'
  context_object_name = 'posts'

  def get_queryset(self):
    return super().get_queryset()

class PostDetailView(DetailView):
  model = Post
  template_name = 'post_detail.html'
  context_object_name = 'post'
  url_kwarg = 'slug'
  # form_class= CommentForm

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['form'] = CommentForm()
    context['comments'] = Comment.objects.filter(post=self.get_object())
    print(context)
    return context
  
  def post(self,request, *args, **kwargs):
    form = CommentForm(request.POST or None)
    if form.is_valid():
      post = self.get_object()
      instance = form.save(commit=False)
      instance.created_by = request.user
      instance.post = post
      instance.save()
      return HttpResponseRedirect(reverse_lazy('post:post-detail', kwargs={'slug': post.slug}))

class PostCreateView(CreateView):
  model = Post
  fields = ['title', 'cover', 'content']
  template_name = 'post_create.html'
  # success_url = 'post:post-list'

  def form_valid(self, form):
    print('Here i am')
    instance = form.save(commit=False)
    instance.author = self.request.user
    instance.save()
    return super().form_valid(form)

class PostUpdateView(UpdateView):
  model = Post
  fields = ['title', 'cover', 'content']
  template_name = 'post_create.html'

class PostDeleteView(DeleteView):
  model = Post
  template_name = 'post_delete.html'
  success_url = reverse_lazy('post:post-list')

