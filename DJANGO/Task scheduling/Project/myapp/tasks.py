from __future__ import absolute_import, unicode_literals
from celery import shared_task
from faker import Faker
from .models import Person
import io,csv
from django.http import  HttpResponse

fake = Faker()

@shared_task
def create_fake_data(num):
  for x in range(num):
    Person.objects.create(name= fake.name(), address=fake.text())


# @shared_task
def export_data():
  resp = HttpResponse(content_type= 'text/csv')
  writer = csv.writer(resp)
  writer.writerow(['Name', 'Address'])

  for per in Person.objects.all():
    writer.writerow([per.name, per.address])
  
  resp['Content-Disposition'] = 'attachment; filename="person.csv"'

  return resp
