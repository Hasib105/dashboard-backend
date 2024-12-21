from rest_framework import viewsets
from .models import Category, Product, Order, Transaction, Session, Visitor
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import now, timedelta
from django.db.models import Sum, Count

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




class ChartDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Get the last 30 days range
        today = now().date()
        last_30_days = today - timedelta(days=30)
        
        # Aggregate data for Sessions
        session_data = (
            Session.objects.filter(date__gte=last_30_days)
            .values("date")
            .annotate(
                total_sessions=Sum("session_count"), 
                unique_visitors=Sum("unique_visitors")
            )
            .order_by("date")
        )

        # Aggregate data for Orders
        order_data = (
            Order.objects.filter(order_date__date__gte=last_30_days)
            .values("order_date__date")
            .annotate(
                total_orders=Count("id"),
                total_revenue=Sum("quantity") * Sum("product__price")  # Ensure `product__price` is accessible
            )
            .order_by("order_date__date")
        )
        
        # Aggregate data for Transactions
        transaction_data = (
            Transaction.objects.filter(transaction_date__date__gte=last_30_days)
            .values("transaction_date__date")
            .annotate(total_amount=Sum("amount"))
            .order_by("transaction_date__date")
        )
        
        # Combine data into the response
        data = {
            "sessions": list(session_data),
            "orders": list(order_data),
            "transactions": list(transaction_data),
        }
        return Response(data)