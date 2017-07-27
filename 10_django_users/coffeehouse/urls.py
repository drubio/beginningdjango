from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

from django.core.urlresolvers import RegexURLResolver, RegexURLPattern

class DecoratedURLPattern(RegexURLPattern):
    def resolve(self, *args, **kwargs):
        result = super(DecoratedURLPattern, self).resolve(*args, **kwargs)
        if result:
            result.func = self._decorate_with(result.func)
        return result

class DecoratedRegexURLResolver(RegexURLResolver):
    def resolve(self, *args, **kwargs):
        result = super(DecoratedRegexURLResolver, self).resolve(*args, **kwargs)
        if result:
            result.func = self._decorate_with(result.func)
        return result

def decorated_includes(func, includes, *args, **kwargs):
    urlconf_module, app_name, namespace = includes
    patterns = getattr(urlconf_module, 'urlpatterns', urlconf_module)    
    for item in patterns:
        if isinstance(item, RegexURLPattern):
            item.__class__ = DecoratedURLPattern
            item._decorate_with = func
            
        elif isinstance(item, RegexURLResolver):
            item.__class__ = DecoratedRegexURLResolver
            item._decorate_with = func

    return urlconf_module, app_name, namespace


from django.contrib.auth.decorators import login_required,permission_required,user_passes_test
from django.contrib.auth.models import Group

from coffeehouse.items.urls import urlpatterns as drinks_url_patterns

from coffeehouse.items.urls import urlpatterns as items_url_patterns
from coffeehouse.registration import views as registration_views


urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='homepage.html'),name="homepage"),
    url(r'^about/', include('coffeehouse.about.urls',namespace="about")),
    url(r'^items/', include(items_url_patterns,namespace="items")),    
    url(r'^stores/',decorated_includes(permission_required('stores.add_store'),include('coffeehouse.stores.urls',namespace="stores"))),
    url(r'^online/',include('coffeehouse.online.urls',namespace="online")),
    url(r'^social/',decorated_includes(user_passes_test(lambda u: Group.objects.get(name='Baristas') in u.groups.all()),include('coffeehouse.social.urls',namespace="social"))),        
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/signup/$',registration_views.UserSignUp.as_view(),name="signup"),    
]
