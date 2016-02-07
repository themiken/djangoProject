from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Hello_world, name="hello")
]