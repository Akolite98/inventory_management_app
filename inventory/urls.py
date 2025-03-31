from django.urls import path
from inventory.views import RegisterUserView, LoginView, UserProfileView, LogoutView

urlpatterns = [
    path("auth/register/", RegisterUserView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/user/", UserProfileView.as_view(), name="user-profile"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
]
