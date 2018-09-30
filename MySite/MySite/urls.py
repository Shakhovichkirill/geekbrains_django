"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mainapp.index, name='main'),
    url(r'^catalog/', mainapp.catalog, name='catalog'),
    url(r'^contacts/', mainapp.contacts, name='contacts'),
    url(r'^product1/', mainapp.product1, name='product1'),
    url(r'^product2/', mainapp.product2, name='product2'),
    url(r'^product3/', mainapp.product3, name='product3'),
    url(r'^products/', include('mainapp.urls', namespace='products')),	
]


