"""
URL configuration for tilkynntu_is project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

from signin_login_registration.views import success_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path("tilkynna", include("report_maker.urls")),
    path('signin/', include('signin_login_registration.urls')),
    path('success/', success_view, name='root-success'), 
    path("images/", include("image_endpoint.urls")),
    path("tilkynningar/", include("report_list.urls")),
    path("report_viewer/", include("report_viewer.urls")),
]
