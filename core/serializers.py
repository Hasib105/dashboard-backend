from rest_framework import serializers
from .models import Category, Product, Order, Transaction, Session, Visitor

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'