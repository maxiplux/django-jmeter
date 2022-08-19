from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault


from apps.orders.models import Order, OrderLine
from apps.products.models import Product
from apps.shopping_cart.dtos.models import OrderDto


class OrderLineDtoSerializer(serializers.Serializer):
   product_id = serializers.IntegerField()
   quantity = serializers.FloatField()





class OrderDtoSerializer(serializers.Serializer):

   order_id=serializers.IntegerField(required=False)
   lines = OrderLineDtoSerializer(many=True)


   def create(self, validated_data):
      """
      Create and return a new `Snippet` instance, given the validated data.
      """
      order=Order()
      order.user=  self.context.get("request").user
      order.save()
      order_lines=[]
      for line in validated_data['lines']:
         order_line=OrderLine()
         order_line.order=order
         order_line.product_id = line['product_id']
         order_line.quantity = line['quantity']
         order_line.save()
         order_lines.append(order_line)
      return self.build_result(order, order_lines)

   def build_result(self,order, order_line):
      return OrderDto(order,order_line)



