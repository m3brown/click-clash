from django.conf.urls import url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from game.views import index, play


urlpatterns = [
    url(r'^$', index),
    url(r'^play$', play),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(
            template_name='registration/login.html'
    )),
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view()),
    url('^accounts/register/$', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/play'
    )),
]
