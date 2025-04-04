from venv import logger
from django.db.models import F
from django.contrib.auth.models import User
from rest_framework import generics, permissions, filters
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from inventory import models
from inventory import serializers
from inventory.serializers import UserSerializer
from inventory.models import InventoryItem
from inventory.serializers import InventorySerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import InventoryItem
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
import logging
logger = logging.getLogger(__name__)



# User Registration
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Add this line

# Login - Get JWT Token
class LoginView(generics.GenericAPIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response(
                {"refresh": str(refresh), "access": str(refresh.access_token)}
            )
        return Response({"error": "Invalid credentials"}, status=400)

# Get User Profile
class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

# Logout (Blacklist Token) - Optional
class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully"}, status=200)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=400)
class InventoryPagination(PageNumberPagination):
    """Paginate inventory items (5 per page)"""
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50

class InventoryListView(generics.ListAPIView):
    """Retrieve inventory items (with search and pagination)"""
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = InventoryPagination

    # Enable search filtering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['quantity']
    search_fields = ['name']

    def get_queryset(self):
        """Filter items belonging to the authenticated user"""
        return InventoryItem.objects.filter(owner=self.request.user)


class InventoryCreateView(generics.CreateAPIView):
    """Create a new inventory item"""
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class InventoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete an inventory item with improved error handling"""
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Ensure users can only access their own items"""
        return InventoryItem.objects.filter(owner=self.request.user)

    def get_object(self):
        """Handle cases where an item does not exist"""
        try:
            return super().get_object()
        except InventoryItem.DoesNotExist:
            raise NotFound("The requested inventory item was not found.")
        

class LowStockItemsView(generics.ListAPIView):
    """Retrieve all items that are low in stock."""
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return InventoryItem.objects.filter(
            owner=self.request.user,
            quantity__lte=F('low_stock_threshold'),  # Use F() directly
            quantity__gt=0
        )
class OutOfStockItemsView(generics.ListAPIView):
    """Retrieve all out-of-stock items."""
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return InventoryItem.objects.filter(owner=self.request.user, quantity=0)
    
class InventoryReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_items = InventoryItem.objects.filter(owner=request.user).count()
        total_sold = InventoryItem.objects.filter(owner=request.user, quantity=0).count()
        total_available = InventoryItem.objects.filter(owner=request.user).aggregate(Sum('quantity'))['quantity__sum'] or 0

        return Response({
            "total_items": total_items,
            "total_sold": total_sold,
            "total_available_stock": total_available
        })