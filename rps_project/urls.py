"""
URL configuration for rps_project project.

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
# rps_project/urls.py
from django.contrib import admin
from django.urls import path, include # include функциясын кошууну унутпаңыз

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rps/', include('gamecore.urls')), # Биздин gamecore тиркемесинин URL'дарын кошобуз
    # Башкы бет үчүн оюн барагына багыттоо (милдеттүү эмес):
    # from gamecore.views import play_rps_view (жогоруга импорттоп)
    # path('', play_rps_view, name='home_page_rps'), 
]