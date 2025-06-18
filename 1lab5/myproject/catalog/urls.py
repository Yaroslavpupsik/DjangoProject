from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('catalog/', views.ProductListView.as_view(), name='product_list'),
    path('catalog/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('specials/', views.SpecialOffersView.as_view(), name='specials'),
]
