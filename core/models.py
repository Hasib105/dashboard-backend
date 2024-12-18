from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Make the model abstract to prevent it from being created as a table

class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Order(BaseModel):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    customer_email = models.EmailField()
    shipping_address = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')

    @property
    def total_price(self):
        return self.quantity * self.product.price


class Transaction(BaseModel):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
    ]

    order = models.ForeignKey(Order, related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f'Transaction {self.id} - {self.status}'


class Session(models.Model):
    country = models.CharField(max_length=100)
    session_count = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    unique_visitors = models.IntegerField(default=0)

    def __str__(self):
        return f'Sessions in {self.country} on {self.date}'


class Visitor(models.Model):
    session_id = models.CharField(max_length=100, unique=True)
    visited_at = models.DateTimeField(auto_now_add=True)
    user_agent = models.TextField(blank=True)
    referrer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.session_id