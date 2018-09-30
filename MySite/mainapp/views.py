# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import ProductCategory, Product

def index(request):
	return render(request, 'mainapp/index.html')

def catalog(request):
        return render(request, 'mainapp/catalog.html')

def contacts(request):
        return render(request, 'mainapp/contacts.html')

def product1(request):
        return render(request, 'mainapp/product1.html')

def product2(request):
        return render(request, 'mainapp/product2.html')

def product3(request):
        return render(request, 'mainapp/product3.html')

def main(request):
	title = 'главная'
	products = Product.objects.all()[:4]
	content = {'title': title, 'products': products}
	return render(request, 'mainapp/index.html', content)

def products(request, pk=None):
	print(pk)
