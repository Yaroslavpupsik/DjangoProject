from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import Product, Category

class HomePageView(TemplateView):
    template_name = 'catalog/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Головна сторінка'
        context['pages'] = [
            {'title': 'Про нас', 'url_name': 'about'},
            {'title': 'Каталог товарів', 'url_name': 'product_list'},
            {'title': 'Контакти', 'url_name': 'contacts'},
            {'title': 'Акції', 'url_name': 'specials'},
        ]
        context['featured_products'] = Product.objects.filter(is_featured=True)[:4]
        return context

class AboutView(TemplateView):
    template_name = 'catalog/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Про нашу компанію'
        return context

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    
    def get_queryset(self):
        return Product.objects.filter(status='in_stock').order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог товарів'
        context['categories'] = Category.objects.filter(is_active=True)
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['title'] = product.name
        context['related_products'] = Product.objects.filter(
            category=product.category
        ).exclude(id=product.id)[:4]
        return context

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контактна інформація'
        context['contacts'] = {
            'Адреса': 'м. Київ, вул. Прикладна, 123',
            'Телефон': '+380 12 345 6789',
            'Email': 'info@example.com',
            'Графік роботи': 'Пн-Пт: 9:00 - 18:00',
        }
        return context

class SpecialOffersView(TemplateView):
    template_name = 'catalog/specials.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Акції та знижки'
        context['special_offers'] = Product.objects.filter(
            old_price__isnull=False
        ).order_by('-created_at')
        return context
