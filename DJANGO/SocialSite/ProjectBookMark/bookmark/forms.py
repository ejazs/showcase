#for image download
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify

from django import forms
from .models import Image
from django.core.files import File

class ImageCreateForm(forms.ModelForm):
  
  class Meta:
    model = Image
    fields = ['title', 'url', 'description']
    widgets = {
      'url' : forms.HiddenInput,
    }

  def clean_url(self):
    valid_extensions = ['jpg', 'jpeg', 'png']  
    print(self.cleaned_data.get('url'))
    url = self.cleaned_data.get('url')
    if url.split('.')[-1] not in valid_extensions:
      return forms.ValidationError('Not image')
    return url

  def save(self, commit=True):
    form = super(ImageCreateForm, self).save(commit=False)
    image_url = self.cleaned_data.get('url')
    image_name = '{}.{}'.format(slugify(form.title), image_url.split('.')[-1])

    #downloads image from given URL
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 
    req=request.Request(image_url,None,headers) 
    response = request.urlopen(req)
    form.image.save(image_name, ContentFile(response.read()), save=False)

    if commit:
      form.save()
    return form

    