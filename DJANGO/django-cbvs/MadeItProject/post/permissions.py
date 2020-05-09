from django.contrib.auth.mixins import UserPassesTestMixin

class TestMixin1(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.email.endswith('@example.com')



from django.contrib.auth.mixins import PermissionRequiredMixin

class MyView(PermissionRequiredMixin, View):
    permission_required = 'polls.can_vote'
    # Or multiple of permissions:
    permission_required = ('polls.can_open', 'polls.can_edit')


# Sessions
'''

Using database-backed sessions¶ : If you want to use a database-backed session, you need to add 'django.contrib.sessions' to your INSTALLED_APPS setting.


Using cached sessions¶ : To store session data using Django’s cache system, you’ll first need to make sure you’ve configured your cache; see the cache documentation for details.

Using file-based sessions¶ : To use file-based sessions, set the SESSION_ENGINE setting to "django.contrib.sessions.backends.file".

Using cookie-based sessions¶ : To use cookies-based sessions, set the SESSION_ENGINE setting to "django.contrib.sessions.backends.signed_cookies". The session data will be stored using Django’s tools for cryptographic signing and the SECRET_KEY setting.


'''

#Cache 

'''
The Per-Site Cache
UpdateCacheMiddleware : FetchFromCacheMiddleware

The Per-View Cache
@cache_page(60 * 15)

Template Fragment Caching


'''
