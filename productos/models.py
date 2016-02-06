from __future__ import unicode_literals

from django.db import models

class ProductoT(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=6, decimal_places=2)

