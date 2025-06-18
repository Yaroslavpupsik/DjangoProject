from django.core.management.base import BaseCommand
from django.utils import timezone
from catalog.models import Category, Product
import random

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create categories
        categories = [
            'Смартфони',
            'Ноутбуки',
            'Планшети',
            'Навушники',
            'Годинники',
        ]
        
        category_objs = []
        for i, name in enumerate(categories, 1):
            category, created = Category.objects.get_or_create(
                name=name,
                defaults={
                    'slug': f'category-{i}',
                    'description': f'Опис категорії {name}',
                    'sort_order': i * 10,
                }
            )
            category_objs.append(category)
            self.stdout.write(self.style.SUCCESS(f'Created category: {name}'))
        
        # Create products
        products = [
            {
                'name': 'iPhone 13 Pro',
                'price': 39999,
                'old_price': 42999,
                'description': 'Потужний смартфон з камерою Pro',
                'features': 'Діагональ: 6.1"\nПроцесор: Apple A15 Bionic\nПам\'ять: 128 ГБ\nКамера: 12 Мп + 12 Мп + 12 Мп',
                'status': 'in_stock',
                'warranty': 12,
                'quantity': 15,
                'is_featured': True,
                'is_new': True,
            },
            {
                'name': 'Samsung Galaxy S21',
                'price': 28999,
                'old_price': 31999,
                'description': 'Флагманський смартфон від Samsung',
                'features': 'Діагональ: 6.2"\nПроцесор: Exynos 2100\nПам\'ять: 256 ГБ\nКамера: 64 Мп + 12 Мп + 12 Мп',
                'status': 'in_stock',
                'warranty': 12,
                'quantity': 8,
                'is_featured': True,
                'is_new': False,
            },
            {
                'name': 'Xiaomi Redmi Note 10 Pro',
                'price': 12999,
                'old_price': 13999,
                'description': 'Краще співвідношення ціни та якості',
                'features': 'Діагональ: 6.67"\nПроцесор: Snapdragon 732G\nПам\'ять: 128 ГБ\nКамера: 108 Мп + 8 Мп + 5 Мп + 2 Мп',
                'status': 'in_stock',
                'warranty': 24,
                'quantity': 25,
                'is_featured': False,
                'is_new': False,
            },
            {
                'name': 'MacBook Air M1',
                'price': 42999,
                'old_price': 45999,
                'description': 'Найкращий ноутбук для роботи',
                'features': 'Діагональ: 13.3"\nПроцесор: Apple M1\nПам\'ять: 256 ГБ SSD\nОперативна пам\'ять: 8 ГБ',
                'status': 'in_stock',
                'warranty': 24,
                'quantity': 5,
                'is_featured': True,
                'is_new': True,
            },
            {
                'name': 'Dell XPS 13',
                'price': 51999,
                'old_price': 54999,
                'description': 'Преміальний ультрабук з безмежним екраном',
                'features': 'Діагональ: 13.4"\nПроцесор: Intel Core i7\nПам\'ять: 512 ГБ SSD\nОперативна пам\'ять: 16 ГБ',
                'status': 'on_order',
                'warranty': 24,
                'quantity': 0,
                'is_featured': False,
                'is_new': False,
            },
            {
                'name': 'iPad Pro 12.9',
                'price': 46999,
                'old_price': 49999,
                'description': 'Потужний планшет для професійної роботи',
                'features': 'Діагональ: 12.9"\nПроцесор: Apple M1\nПам\'ять: 256 ГБ\nПідтримка Apple Pencil',
                'status': 'in_stock',
                'warranty': 12,
                'quantity': 7,
                'is_featured': True,
                'is_new': True,
            },
            {
                'name': 'Samsung Galaxy Tab S7',
                'price': 28999,
                'old_price': 30999,
                'description': 'Потужний Android-планшет',
                'features': 'Діагональ: 11"\nПроцесор: Snapdragon 865+\nПам\'ять: 128 ГБ\nПідтримка S Pen',
                'status': 'in_stock',
                'warranty': 12,
                'quantity': 12,
                'is_featured': False,
                'is_new': False,
            },
            {
                'name': 'AirPods Pro',
                'price': 8999,
                'old_price': 9999,
                'description': 'Бездротові навушники з активним шумозаглушенням',
                'features': 'Тип: Бездротові\nАктивне шумозаглушення\nЧас роботи: 4.5 год\nКейс для заряджання',
                'status': 'in_stock',
                'warranty': 12,
                'quantity': 30,
                'is_featured': True,
                'is_new': False,
            },
            {
                'name': 'Sony WH-1000XM4',
                'price': 14999,
                'old_price': 15999,
                'description': 'Преміальні бездротові навушники',
                'features': 'Тип: Бездротові\nАктивне шумозаглушення\nЧас роботи: 30 год\nСенсорне керування',
                'status': 'in_stock',
                'warranty': 24,
                'quantity': 10,
                'is_featured': True,
                'is_new': True,
            },
            {
                'name': 'Apple Watch Series 7',
                'price': 18999,
                'old_price': 19999,
                'description': 'Розумний годинник з великим дисплеєм',
                'features': 'Діагональ: 1.69"\nВодонепроникність 50м\nМоніторинг сну\nКисневі датчики',
                'status': 'in_stock',
                'warranty': 12,
                'quantity': 18,
                'is_featured': True,
                'is_new': True,
            },
        ]
        
        for i, product_data in enumerate(products, 1):
            # Select a random category
            category = random.choice(category_objs)
            
            # Create product
            product = Product.objects.create(
                name=product_data['name'],
                slug=f'product-{i}',
                category=category,
                price=product_data['price'],
                old_price=product_data['old_price'],
                description=product_data['description'],
                features=product_data['features'],
                status=product_data['status'],
                warranty=product_data['warranty'],
                quantity=product_data['quantity'],
                is_featured=product_data['is_featured'],
                is_new=product_data['is_new'],
            )
            
            self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database!'))
