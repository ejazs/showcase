from django.shortcuts import render, get_object_or_404
from .models import Note
from .forms import CreateNotesForm
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@csrf_protect
def notes(request):
  form = CreateNotesForm(request.POST or None )
  if request.is_ajax():
    print('form is_valid', form.is_valid())
    if form.is_valid():
      instance = form.save(commit=False)
      instance.created_by = request.user
      instance.save()
      resp = {'success': 'object saved!'}
      return JsonResponse(resp)
    else:
      print(form)
      resp = {'errors': 'jaaz'}
      return JsonResponse(resp)
  notes = Note.objects.all()
  context = {'form':form, 'notes':notes}
  return render(request, 'home.html', context)

def set_is_completed(request, id):
  if request.is_ajax():
    obj = get_object_or_404(Note, id=id)
    obj.status = not obj.status
    obj.save()
    print(obj)
    resp = {'status':'ok'}
    return JsonResponse(resp)
    