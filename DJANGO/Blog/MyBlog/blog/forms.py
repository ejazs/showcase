from django import forms
from .models import Post, Comment, Tag
from django.forms import BooleanField

class PostForm(forms.ModelForm):
  # status = BooleanField()
  tags = forms.CharField(help_text='Enter comma seprated tags')
  class Meta:
    model = Post
    fields = ['title', 'status', 'body', 'publish', 'tags']

  # def is_valid(self):
  #   print('FROM FORM', self.changed_data)
  #   return super().is_valid()

class PostShare(forms.Form):
  name = forms.CharField(max_length=120)
  your_email = forms.EmailField()
  friend_email = forms.EmailField()
  message = forms.TextInput(attrs={"required":"false"})


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['body', 'name', 'email']