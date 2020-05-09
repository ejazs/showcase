from django.urls import path
from .views import CreateFakeDataView, download,large_csv

app_name = 'myapp'

urlpatterns = [
  path('', CreateFakeDataView.as_view(), name='home'),
  path('download/', large_csv, name='download')
]