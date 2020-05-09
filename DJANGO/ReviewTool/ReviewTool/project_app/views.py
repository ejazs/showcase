from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Project
from .tables import ProjectTable
from .filters import ProjectFilter
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .forms import ProjectForm
# Create your views here.
from django_tables2 import SingleTableView



class ProjectListView(SingleTableMixin, FilterView):
  model = Project
  table_class = ProjectTable
  template_name = 'project_list.html'
  filterset_class = ProjectFilter
  table_pagination = {
        "per_page": 10
    }	
  extra_context = {
    'name':'ehaz'
  }

  # def get_context_data(self, *args, **kwargs):
  #   context = super(ProjectListView, self).get_context_data(*args, **kwargs)
  #   context['project_filter'] = ProjectFilter(self.request.GET, queryset=Project.objects.all())
  #   print(context)
  #   return context



  # def get_queryset(self, *args, **kwargs):
  #   qs = super(ProjectListView, self).get_queryset(*args, **kwargs)
  #   qs['project_filter'] = ProjectFilter(self.request.GET, queryset=Project.objects.all())
  #   print(qs)
  #   return qs

class ProjectCreateView(CreateView):
  model = Project
  form_class = ProjectForm
  template_name = 'project_create.html'

  def form_valid(self, form):
    print('called')
    instance = form.save(commit=False)
    instance.created_by = self.request.user
    instance.updated_by = self.request.user
    return super().form_valid(form)
  
  def form_invalid(self, form):
    print(form)
    return super().form_invalid(form)

class ProjectDetailView(DetailView):
  model = Project
  template_name = 'project_detail.html'