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
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views
from .views import home

urlpatterns = [
    # path('', include('blog.urls')),  # http://127.0.0.1:8000/はどうするのか
    path('blog/', include('blog.urls')),
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
    # https://qiita.com/moi1990sk/items/a849fca7acb29db95508
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('', home, name='home'),
]

LOGIN_URL = 'login/'
LOGIN_REDIRECT_URL = ''

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '192845778622-g61ftg21hsfh3ju9mcvevslqfnkjlj5u.apps.googleusercontent.com'  #Paste CLient Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'YnUx9PSn2rvZrwBiWdJPQ2o8' #Paste Secret Key