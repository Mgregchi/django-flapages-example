"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# re_path
from django.urls import path, include

# from django.contrib.flatpages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    
]
# django.pdf#subsection.6.5.4
"""
urlpatterns += [
    re_path(r'^(?P<url>.*/)$',
            fp_views.flatpage),
]
"""
'''
urlpatterns += [
    path('about-us/', views.flatpage, {'url': '/about-us/'}, name='about'),
    path('license/', views.flatpage, {'url': '/license/'}, name='license'),
    path('privacy/', views.flatpage, {'url': '/privacy/'}, name='privacy'),
]
'''
