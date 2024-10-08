"""
URL configuration for merchex project.

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
from django.urls import path
from listings import views
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
	path('bands/', views.band_list, name='band-list'),
	path('bands/<int:id>/', views.band_detail, name='band-detail'),
	path('bands/add/', views.band_create, name='band-create'),
	path('about-us/', views.about, name='about'),
	path('listings/', views.listing_list, name='listing-list'),
	path('listings/<int:id>/', views.listing_detail, name='listing-detail'),
	path('listings/add/', views.listing_create, name='listing-create'),
	path('contact-us/', views.contact, name='contact'),
	path('', lambda request: HttpResponseRedirect('/bands/')), # redirect home on a page
	path('email-sent/', views.email_sent, name='email-sent')
]

handler404 = 'listings.views.error404'
