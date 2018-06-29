from django.conf.urls import include, url


from django.conf.urls import include, url
from django.contrib import admin

from rooms import urls
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
	#url(r'^$', room_views.login, name='login'),
    url(r'^hcmf/', admin.site.urls),
    url(r'^rooms/', include(urls, namespace="rooms")),
    url(r'^accounts/login/', login, {'template_name':'login/index.html'}, name="login"),
    url(r'^$', login, {'template_name':'login/index.html'}, name="login"),
    url(r'^logout/', logout_then_login, name="logout"),
    
]

