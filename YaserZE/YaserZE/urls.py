"""
URL configuration for YaserZE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ تعريف التطبيقات الثلاثة:
    path('store/', include('store.urls')),
    path('orders/', include('orders.urls')),
    path('accounts/', include('accounts.urls')),
]
