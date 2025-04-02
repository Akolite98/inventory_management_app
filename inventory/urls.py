from django.urls import path
from inventory.views import RegisterUserView, LoginView, UserProfileView, LogoutView
from inventory.views import InventoryListCreateView, InventoryDetailView
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import LowStockItemsView, OutOfStockItemsView
from .views import InventoryReportView

urlpatterns = [
    path("auth/register/", RegisterUserView.as_view(), name="register"),
    path("auth/login/", TokenObtainPairView.as_view(), name="login"),
    path("auth/user/", UserProfileView.as_view(), name="user-profile"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),

        # Inventory CRUD endpoints
    path("inventory/", InventoryListCreateView.as_view(), name="inventory-list"),
    path("inventory/<int:pk>/", InventoryDetailView.as_view(), name="inventory-detail"),

    path('api/inventory/low-stock/', LowStockItemsView.as_view(), name='low_stock_items'),
    path('api/inventory/out-of-stock/', OutOfStockItemsView.as_view(), name='out_of_stock_items'),
     path('inventory/reports/', InventoryReportView.as_view(), name='inventory-reports'),
]
