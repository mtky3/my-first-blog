"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin

from django.contrib.auth import views

urlpatterns = [
    # path('', include('blog.urls')),  # http://127.0.0.1:8000/はどうするのか
    path('post/', include('blog.urls')),
    # https://docs.djangoproject.com/ja/2.2/intro/tutorial01/
    path('polls/', include('polls.urls')),
    # https://qiita.com/kaki_k/items/6e17597804437ef170ae
    path('cms/', include('cms.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    # https://it-engineer-lab.com/archives/544
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
]

