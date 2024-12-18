import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.models import Category, Product, Order, Transaction, Session, Visitor

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # Create superuser
        User.objects.create_superuser(
            username='admin',
            password='admin',
            email='admin@mail.com'
        )
        self.stdout.write(self.style.SUCCESS('Superuser created.'))

        # Create normal users
        for i in range(10):
            User.objects.create_user(
                username=f'user{i}',
                password='password123',
                email=f'user{i}@mail.com'
            )
        self.stdout.write(self.style.SUCCESS('10 normal users created.'))

        # Create categories
        categories = []
        for i in range(5):
            category = Category.objects.create(name=f'Category {i}')
            categories.append(category)
        self.stdout.write(self.style.SUCCESS('5 categories created.'))

        # Create products
        products = []
        for i in range(50):
            product = Product.objects.create(
                name=f'Product {i}',
                category=random.choice(categories),
                price=random.uniform(10.0, 100.0),
                stock=random.randint(1, 100)
            )
            products.append(product)
        self.stdout.write(self.style.SUCCESS('50 products created.'))

        # Create orders
        for i in range(50):
            product = random.choice(products)
            quantity = random.randint(1, 5)
            Order.objects.create(
                product=product,
                quantity=quantity,
                customer_email=f'customer{i}@mail.com',
                shipping_address=f'Address {i}',
                status=random.choice(['pending', 'shipped', 'delivered', 'cancelled'])
            )
        self.stdout.write(self.style.SUCCESS('50 orders created.'))

        # Create transactions
        for order in Order.objects.all():
            Transaction.objects.create(
                order=order,
                amount=order.total_price,
                status=random.choice(['completed', 'pending', 'failed']),
                payment_method=random.choice(['credit_card', 'paypal'])
            )
        self.stdout.write(self.style.SUCCESS('Transactions created for all orders.'))

        # Create sessions
        for i in range(30):
            Session.objects.create(
                country=f'Country {i}',
                session_count=random.randint(10, 100),
                unique_visitors=random.randint(1, 50)
            )
        self.stdout.write(self.style.SUCCESS('30 sessions created.'))

        # Create visitors
        for i in range(100):
            Visitor.objects.create(
                session_id=f'session-{i}',
                user_agent='Mozilla/5.0',
                referrer='http://example.com'
            )
        self.stdout.write(self.style.SUCCESS('100 visitors created.'))

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))