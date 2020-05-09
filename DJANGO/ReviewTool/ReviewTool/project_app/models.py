from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.

User = settings.AUTH_USER_MODEL

class Project(models.Model):
  STATE_CHOICES = (
    ('active', 'Active'),
    ('inactive', 'InActive')
  )
  project_id = models.CharField(max_length=255, null=True, blank=True)
  name = models.CharField(max_length=255)
  business_field = models.CharField(max_length=255, null=True, blank=True)
  customer = models.CharField(max_length=255, null=True, blank=True)
  lead = models.ForeignKey(User,on_delete=models.CASCADE)
  start_date = models.DateField()
  end_date   = models.DateField()
  viewers = models.ManyToManyField(User, related_name='viewer')
  creators = models.ManyToManyField(User, related_name='creator')
  comment = models.TextField(null=True, blank=True)

  state = models.CharField(max_length=255, choices = STATE_CHOICES, default='active')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='createdby')
  updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updatedby')
  last_activity = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return str(self.name)
  
  def save(self, *args, **kwargs):
    if self.project_id is None:
      super(Project, self).save(*args, **kwargs)
      self.project_id = 'P'+str(self.id).zfill(4)
      super(Project, self).save(*args, **kwargs)
    else:
      super(Project, self).save(*args, **kwargs)
  
  def clean(self, *args, **kwargs):
    if self.end_date < self.start_date:
      raise ValidationError('End date cannot be less than Start date')
    super(Project, self).clean(*args, **kwargs)




