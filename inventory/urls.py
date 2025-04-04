from django.urls import path
from inventory.views import RegisterUserView, LoginView, UserProfileView, LogoutView
from inventory.views import InventoryDetailView
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import LowStockItemsView, OutOfStockItemsView
from .views import InventoryReportView
from .views import InventoryListView, InventoryCreateView

urlpatterns = [
    path("auth/register/", RegisterUserView.as_view(), name="register"),
    path("auth/login/", TokenObtainPairView.as_view(), name="login"),
    path("auth/user/", UserProfileView.as_view(), name="user-profile"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),

    path('inventory/', InventoryListView.as_view(), name='inventory-list'),
    path('inventory/create/', InventoryCreateView.as_view(), name='inventory-create'),
    path("inventory/<int:pk>/", InventoryDetailView.as_view(), name="inventory-detail"),
    
    # Changed these:
    path('inventory/low-stock/', LowStockItemsView.as_view(), name='low_stock_items'),
    path('inventory/out-of-stock/', OutOfStockItemsView.as_view(), name='out_of_stock_items'),
    path('inventory/reports/', InventoryReportView.as_view(), name='inventory-reports'),
]