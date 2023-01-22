"""homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from pair_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exchange/', views.show_exchange),
    path('exchange/add/<name>/', views.add_exchange),
    path('exchange/delete/<id>/', views.delete_exchange),
    path('exchange/update/<id>/<name>/', views.update_exchange),
    path('pair/', views.show_pair),
    path('pair/add/<symbol>/<ask>/<bid>/<exchange_id>/', views.add_pair),
    path('pair/delete/<id>/', views.delete_pair),
    path('pair/update/<id>/<symbol>/<ask>/<bid>/<exchange_id>', views.update_pair),
    path('', views.show_pair)
]
