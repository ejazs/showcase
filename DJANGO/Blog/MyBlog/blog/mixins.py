from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse, HttpResponseForbidden, Http404

class UserIsAuthorMixin(UserPassesTestMixin):

  def test_func(self):
    post = self.get_object()
    return self.request.user == post.author

  def handle_no_permission(self):
        """ Do whatever you want here if the user doesn't pass the test """
        raise Http404