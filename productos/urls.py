from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Hello_world, name="hello"),
	url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail),
	url(r'^product/new', views.NewProduct, name="NewProduct")
]