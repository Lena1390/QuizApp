from django.urls import path

from account import views

urlpatterns = [
    path('', views.web, name='home'),
    path('site', views.site, name='site')
]