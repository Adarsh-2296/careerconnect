"""
URL configuration for careerconnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('register/', views.print_hello, name='stdregister'),
    path('alulogin/', views.alulogin, name='alulogin'),
    path('alumnipro/', views.alumnipro, name='alumnipro'),
    path('alumniproedit/', views.alumniproedit, name='alumniproedit'),
    path('deptlogin/', views.deptlogin, name='deptlogin'),
    path('main/', views.main, name='main'),
    path('accounts/login/', views.login, name='login'),
    path('studentpro/', views.studentpro, name='studentpro'),
    path('forgotps/', views.forgotps, name='forgotps'),
    path('stdproedit/', views.stdproedit, name='stdproedit')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

