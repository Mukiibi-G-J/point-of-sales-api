from rest_framework import serializers
from .models import Sales





class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ('id', 'date', 'product', 'quantity', 'price', 'profit', 'total', 'discount', 'customer')