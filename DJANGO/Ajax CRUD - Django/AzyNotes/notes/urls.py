from django.urls import path
from .views import notes, set_is_completed

app_name = 'notes'

urlpatterns = [
  path('', notes, name='notes'),
  path('notes/<id>/', set_is_completed, name='set_is_completed')
]
