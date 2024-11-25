from django.core.management.base import BaseCommand
from products.models import Product, Category
from django.core.files import File
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Populate the database with sample products and categories'

    def handle(self, *args, **kwargs):
        # Clear existing products and categories
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Create categories
        categories = [
            Category.objects.create(name="Electronics"),
            Category.objects.create(name="Clothing"),
            Category.objects.create(name="Books"),
            Category.objects.create(name="Home & Kitchen"),
        ]

        # Sample product data
        products = [
            {
                'name': 'Laptop',
                'price': 999.99,
                'description': 'High-performance laptop with the latest specs.',
                'stock': 50,
                'image': 'laptop.jpg',
                'category': categories[0]  # Electronics
            },
            {
                'name': 'Smartphone',
                'price': 699.99,
                'description': 'Latest smartphone with advanced camera features.',
                'stock': 100,
                'image': 'smartphone.jpg',
                'category': categories[0]  # Electronics
            },
            {
                'name': 'T-Shirt',
                'price': 19.99,
                'description': 'Comfortable cotton t-shirt in various colors.',
                'stock': 200,
                'image': 't-shirt.jpg',
                'category': categories[1]  # Clothing
            },
            {
                'name': 'Novel',
                'price': 14.99,
                'description': 'Bestselling fiction novel.',
                'stock': 75,
                'image': 'novel.jpg',
                'category': categories[2]  # Books
            },
            {
                'name': 'Coffee Maker',
                'price': 79.99,
                'description': 'Programmable coffee maker with multiple brew settings.',
                'stock': 30,
                'image': 'coffee-maker.jpg',
                'category': categories[3]  # Home & Kitchen
            },
        ]

        for product_data in products:
            product = Product.objects.create(
                name=product_data['name'],
                price=product_data['price'],
                description=product_data['description'],
                stock=product_data['stock'],
                category=product_data['category']
            )
            
            # Handle image
            image_path = os.path.join(settings.MEDIA_ROOT, 'sample_images', product_data['image'])
            if os.path.exists(image_path):
                with open(image_path, 'rb') as image_file:
                    product.image.save(product_data['image'], File(image_file), save=True)
            else:
                self.stdout.write(self.style.WARNING(f"Image not found: {image_path}"))

            self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))

        self.stdout.write(self.style.SUCCESS('Database populated successfully with products and categories'))

