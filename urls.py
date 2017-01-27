from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<track_key>[^/]+)$', views.trace, name='track'),
 	url(r'^mail/new/?$', views.new_mail, name='track'),   
]