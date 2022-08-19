from rest_framework import viewsets, permissions

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer

    permission_classes = [permissions.IsAuthenticated]