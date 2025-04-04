from django.contrib.auth.models import User
from rest_framework import serializers
from inventory.models import InventoryItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class InventorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_low_stock = serializers.SerializerMethodField()
    is_out_of_stock = serializers.SerializerMethodField()

    class Meta:
        model = InventoryItem
        fields = '__all__'

    def get_is_low_stock(self, obj):
        return obj.is_low_stock()

    def get_is_out_of_stock(self, obj):
        return obj.is_out_of_stock()