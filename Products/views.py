from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from .serializer import ProductSerializer, StaffSerializer
from .models import Product, Staff

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.staff.all()
    serializer_class = StaffSerializer