"""
URL configuration for CSKPromos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('year/<int:wyear>', views.yearselect, name='yearselect'),
    path('year/2023/card/<int:fc>', views.video2023, name='video2023'),
    path('year/2024/card/<int:fc>', views.video2024, name='video2024'),
    path('year/2025/card/<int:fc>', views.video2025, name='video2025'),
]
