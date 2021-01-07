
from django.contrib import admin
from django.urls import path
from myApp import views
from django.conf.urls import url

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', views.post_list_view),


]
