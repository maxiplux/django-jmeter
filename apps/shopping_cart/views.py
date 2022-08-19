# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from apps.shopping_cart.serializers import OrderDtoSerializer


class ShoppingCartView(ViewSet):
    serializer_class = OrderDtoSerializer
    http_method_names = ['post', ]


    def create(self, request):

        serializer = OrderDtoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
