from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Order
from .serializers import OrderCreateSerializer, OrderListSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def create(self, request, *args, **kwargs):
        write_serializer = OrderCreateSerializer(data=request.data)
        write_serializer.is_valid(raise_exception=True)
        instance = self.perform_create(write_serializer)
        read_serializer = OrderListSerializer(instance)

        print(instance)
        return Response(read_serializer.data)