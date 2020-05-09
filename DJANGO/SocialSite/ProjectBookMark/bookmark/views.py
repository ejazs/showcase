from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ImageCreateForm
from django.views.generic import CreateView
from django.core.files import File
from django.contrib.auth.mixins import LoginRequiredMixin
import urllib, requests
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
# Create your views here.

class Home(TemplateView):
  template_name = 'base.html'


def image_create_view(request):
  form = ImageCreateForm(request.POST or None)
  if request.POST:
    if form.is_valid():
      instance = form.save(commit=False)
      instance.user = request.user
      form.save()
      return HttpResponseRedirect('/')
  else:
    form = ImageCreateForm(request.GET)

  context = {'form':form}

  return render(request, 'image_form.html', context)

class ImageCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  http_method_names = ['get', 'post', 'head', 'options', 'trace']
  template_name = 'image_form.html'
  form_class = ImageCreateForm
  success_message = 'Image added successfully!'
  #initial = {'title':'Ejaz'}

  def get_initial(self):
    title = self.request.GET.get('title')
    url   = self.request.GET.get('url')
    data = super(ImageCreateView, self).get_initial()
    data['title'] = title
    data['url'] = url
    return data

  def form_valid(self, form):
    print('Hele')
    instance = form.save(commit = False)
    instance.user = self.request.user
    instance.save()
    return super(ImageCreateView, self).form_valid(form)

  def form_invalid(self, form):
    print('ERORORORORO', form.errors)
    return super().form_invalid(form)

  # def get(self, request, *args, **kwargs):
  #   form_class = self.get_form_class()
  #   self.object = None
  #   form = form_class(request_data=request)
  #   #return super(ImageCreateView, self).get(request, *args, **kwargs)
  #   return self.render_to_response(self.get_context_data(form=form))
  
