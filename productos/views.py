from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import ProductoT

# Create your views here.
def Hello_world(request):
	product = ProductoT.objects.order_by('id')
	template = loader.get_template('index.html')
	context = {
		'product' : product
	}
	return HttpResponse(template.render(context, request))
