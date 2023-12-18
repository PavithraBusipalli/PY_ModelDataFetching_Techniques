"""
URL configuration for project26 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('insert_course/',insert_course,name='insert_course'),
    path('insert_student/',insert_student,name='insert_student'),
    path('insert_accessRecord',insert_accessRecord,name='insert_accessRecord'),
    path('display_course/',display_course,name='display_course'),
    path('display_student/',display_student,name='display_student'),
    path('display_accessRecord/',display_accessRecord,name='display_accessRecord'),
]
