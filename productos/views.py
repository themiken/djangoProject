from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
from .models import ProductoT

# Create your views here.
def Hello_world(request):
	product = ProductoT.objects.order_by('id')
	template = loader.get_template('index.html')
	context = {
		'product' : product
	}
	return HttpResponse(template.render(context, request))


def ProductDetail(request, pk):
	product = get_object_or_404(ProductoT, pk=pk)
	template = loader.get_template('product_detail.html')
	context = {
		'product': product
	}
	return HttpResponse(template.render(context, request))


def NewProduct(request):
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			product = form.save()
			product.save()
			return HttpResponseRedirect('/')
	else:
		form = ProductForm()

	template = loader.get_template('new_product.html')
	context = {
		'form': form
	}
	return HttpResponse(template.render(context, request))