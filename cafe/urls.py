from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('meni/', views.menu, name='menu'),
    path('za-nas/', views.about, name='about'),
    path('galerija/', views.gallery, name='gallery'),
    path('novosti/', views.news, name='news'),
    path('novosti/<int:pk>/', views.news_detail, name='news_detail'),
    path('kontakt/', views.contact, name='contact'),
    path('rezervacija/', views.reservation, name='reservation'),
    path('privatnost/', views.privacy, name='privacy'),
]
