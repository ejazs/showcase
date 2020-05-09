from django.urls import path
from .views import DashboardView

app_name = 'dashboard_app'

urlpatterns = [
  path('', DashboardView.as_view(), name='dashboard')
]