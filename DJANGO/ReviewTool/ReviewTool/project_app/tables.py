import django_tables2 as tables
from .models import Project



class ProjectTable( tables.Table):
  lead = tables.Column(accessor='lead.get_full_name')
  
  class Meta:
    model = Project
    template_name = "django_tables2/bootstrap.html"
    fields = ['project_id', 'name', 'state', 'business_field', 'customer', 'lead', 'start_date','end_date','last_activity']


