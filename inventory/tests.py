from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from inventory.models import InventoryItem

User = get_user_model()

class InventorySearchFilterTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.force_authenticate(user=self.user)
        InventoryItem.objects.create(name="Laptop", quantity=5, price=500, owner=self.user)
        InventoryItem.objects.create(name="Mouse", quantity=10, price=50, owner=self.user)

    def test_search_inventory(self):
        response = self.client.get("/api/inventory/?search=Laptop")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Laptop")

    def test_filter_inventory_by_quantity(self):
        response = self.client.get("/api/inventory/?quantity=10")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Mouse")
