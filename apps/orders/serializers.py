from rest_framework import serializers

from apps.orders.models import Order, OrderLine


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['created_at','user']


class OrderLineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderLine
        fields = ['order', 'product','quantiy']