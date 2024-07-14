from rest_framework import serializers
from .models import Product, Staff

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = '__all__'
    

class StaffSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Staff
        fields = ['username', 'password',]