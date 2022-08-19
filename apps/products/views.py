from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer

    permission_classes = [permissions.IsAuthenticated]