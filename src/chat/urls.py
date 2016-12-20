from django.conf.urls import url
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^$',  views.about, name='about'),
    url(r'^new/$', views.new_room, name='new_room'),
    url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
    url(r'^admin/', admin.site.urls),
]
