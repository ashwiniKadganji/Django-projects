"""miniblog URL Configuration

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
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home),
    path('about/',views.About,name='about'),
    path('contact/',views.Contact,name='contact'),
    path('dashboard/',views.Dashboard,name='dashboard'),
    path('logout/',views.User_Logout,name='logout'),
    path('login/',views.User_Login,name='login'),
    path('signup/',views.User_Signup,name='signup'),
    path('addpost/',views.add_post,name='addpost'),
    path('updatepost/<int:id>/',views.update_post,name='updatepost'),
    path('delete/<int:id>/',views.delete_post,name='deletepost'),
    
]
