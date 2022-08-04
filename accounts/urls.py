
from django.urls import path

from accounts.views import LoginSiteView, LogoutSiteView, RegisterUserView, FavoriteSkinsView

urlpatterns = [
    path('login/', LoginSiteView.as_view(), name='login'),
    path('logout/', LogoutSiteView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile/', FavoriteSkinsView.as_view(), name='profile'),
]
