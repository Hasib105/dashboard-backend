from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, ProductViewSet, OrderViewSet, 
    TransactionViewSet, SessionViewSet, VisitorViewSet, ChartDataAPIView
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'sessions', SessionViewSet, basename='session')
router.register(r'visitors', VisitorViewSet, basename='visitor')

urlpatterns = router.urls + [
    path('chart-data/', ChartDataAPIView.as_view(), name='chart-data'),
]
