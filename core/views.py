from rest_framework import viewsets
from .models import Category, Product, Order, Transaction, Session, Visitor
from .serializers import (
    CategorySerializer, ProductSerializer, OrderSerializer, 
    TransactionSerializer, SessionSerializer, VisitorSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
