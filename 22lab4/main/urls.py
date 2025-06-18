from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('contacts/', views.contacts, name='contacts'),
] 