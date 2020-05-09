from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):

  message = 'You are not allowed to edit this.'

  def has_object_permission(self, request, view, obj):
    # returns ok if its a GET or HEAD request
    if request.method in SAFE_METHODS:
      return True
      
    return  obj.author == request.user
