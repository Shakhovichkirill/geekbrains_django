# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import ProductCategory, Product
admin.site.register(ProductCategory)
admin.site.register(Product)
