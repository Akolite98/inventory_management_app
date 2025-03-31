from django.contrib.auth.models import User
from rest_framework import serializers
from inventory.models import InventoryItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

        
class InventorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = InventoryItem
        fields = ["id", "name", "description", "quantity", "price", "owner"]
