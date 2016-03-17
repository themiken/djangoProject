from django import forms
from .models import ProductoT

class ProductForm(forms.ModelForm):
	class Meta:
		model = ProductoT
		fields = '__all__'

