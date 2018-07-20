from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^wish$', views.wish),
    url(r'^login_fun$', views.login_fun),
    url(r'^add$', views.add),
    url(r'^add_fun$', views.add_fun),
    url(r'^destroy$', views.destroy),
    url(r'^info$', views.info),
    url(r'^logout$', views.logout),   
]