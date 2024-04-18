from django.urls import path
from apps.products.views import ProductViewSet


urlpatterns = [
    path('api/product/', ProductViewSet.as_view(), name='api_product')
]
