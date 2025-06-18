from django.db import models
from django.urls import reverse
from django.utils import timezone

class Category(models.Model):
    name = models.CharField('Назва категорії', max_length=200, unique=True)
    slug = models.SlugField('URL', max_length=200, unique=True)
    description = models.TextField('Опис', blank=True)
    is_active = models.BooleanField('Активна', default=True)
    created_at = models.DateTimeField('Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField('Дата оновлення', auto_now=True)
    sort_order = models.PositiveIntegerField('Порядок сортування', default=0)
    
    class Meta:
        verbose_name = 'категорія'
        verbose_name_plural = 'категорії'
        ordering = ['sort_order', 'name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

class Product(models.Model):
    STATUS_CHOICES = [
        ('in_stock', 'В наявності'),
        ('out_of_stock', 'Немає в наявності'),
        ('on_order', 'Під замовлення'),
    ]
    
    WARRANTY_CHOICES = [
        (6, '6 місяців'),
        (12, '1 рік'),
        (24, '2 роки'),
        (36, '3 роки'),
    ]
    
    name = models.CharField('Назва товару', max_length=255)
    slug = models.SlugField('URL', max_length=255, unique=True)
    category = models.ForeignKey(Category, verbose_name='Категорія', on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField('Ціна', max_digits=10, decimal_places=2)
    old_price = models.DecimalField('Стара ціна', max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField('Опис', blank=True)
    features = models.TextField('Характеристики', blank=True)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='in_stock')
    warranty = models.PositiveSmallIntegerField('Гарантія (місяців)', choices=WARRANTY_CHOICES, default=12)
    quantity = models.PositiveIntegerField('Кількість', default=1)
    created_at = models.DateTimeField('Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField('Дата оновлення', auto_now=True)
    is_featured = models.BooleanField('Рекомендований', default=False)
    is_new = models.BooleanField('Новинка', default=False)
    
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товари'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})
    
    def get_status_display_class(self):
        status_classes = {
            'in_stock': 'text-success',
            'out_of_stock': 'text-danger',
            'on_order': 'text-warning',
        }
        return status_classes.get(self.status, '')
    
    @property
    def get_discount_percent(self):
        """Повертає відсоток знижки, якщо є стара ціна"""
        if self.old_price and self.old_price > self.price:
            return ((self.old_price - self.price) / self.old_price) * 100
        return 0
    
    @property
    def get_discount_amount(self):
        """Повертає суму знижки, якщо є стара ціна"""
        if self.old_price and self.old_price > self.price:
            return self.old_price - self.price
        return 0
    
    def save(self, *args, **kwargs):
        if self.quantity <= 0 and self.status != 'out_of_stock':
            self.status = 'out_of_stock'
        elif self.quantity > 0 and self.status == 'out_of_stock':
            self.status = 'in_stock'
        super().save(*args, **kwargs)
