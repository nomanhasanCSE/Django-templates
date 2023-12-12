from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='homepage',),
    path('about/', views.about, name='aboutpage',),
    path('form/', views.submit_form, name='submit_form',),
    path('django_form/', views.Django_form, name='django_form',),
    # path('about/', views.about),
]