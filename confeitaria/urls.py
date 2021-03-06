"""confeitaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django.conf import settings
from customer import views
from encomendas.views import create_encomenda, list_encomendas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', views.customers, name='customers'),
    path('details/', views.details),
    path('customers/create', views.create_customer),
    path('login/', views.login),
    path('equipe/', views.equipe),
    path('', views.main, name='index'),
    path('encomenda/create', create_encomenda),
    path('encomendas/', list_encomendas)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
