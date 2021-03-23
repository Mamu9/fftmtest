"""fftm_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic.base import TemplateView

urlpatterns = [
	path('personna/', include('personna.urls')),
    path('blog', include('blog.urls')),
   # path('a_a/', include('a_a.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

	#url(r'^a_a/', include("a_a.urls", namespace = "a_a")),
    #path('', Loginview,as_view(template_name="home.html"),name='user_login'),
    #url(r'/', login_required(TemplateView.as_view(template_name="home.html"))),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

   # path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]



