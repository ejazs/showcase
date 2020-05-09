from django.shortcuts import render
from .forms import CreateFakeDataForm
from django.views.generic import FormView
from .tasks import create_fake_data, export_data
from .models import Person
from django.contrib.messages.views import SuccessMessageMixin


import csv
from django.http import StreamingHttpResponse
# Create your views here.

class CreateFakeDataView(SuccessMessageMixin, FormView):
  template_name = 'home.html'
  form_class  = CreateFakeDataForm
  success_url = '/'
  success_message = "Created Successfully!!"

  def get_context_data(self, **kwargs):
    # print('context', super().get_context_data(**kwargs))
    return super().get_context_data(**kwargs)

  def form_valid(self, form):
    print(form.cleaned_data.get('numbers'))
    create_fake_data.delay(int(form.cleaned_data.get('numbers')))
    return super().form_valid(form)

  # def form_valid(self, form):
  #   print(form)
  #   return super().form_valid(form)


def download(request):

  export_data()
  return render(request, 'home.html', {})


class DummyFile:
    def write(self, value_to_write):
        return value_to_write


def large_csv(request):
    rows = ([str(i), str(2 * i), str(3 * i)] for i in range(555555))
    writer = csv.writer(DummyFile())
    data = [writer.writerow(row) for row in rows]
    response = StreamingHttpResponse(data, content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="pythoncircle-dot-com.csv"'
    return response