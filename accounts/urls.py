
from django.urls import path

from accounts.views import LoginSiteView, LogoutSiteView, RegisterUserView, ProfileView, ChangePassword, \
    DeleteUser

urlpatterns = [
    path('login/', LoginSiteView.as_view(), name='login'),
    path('logout/', LogoutSiteView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('changepass/', ChangePassword.as_view(), name='change_pass'),
    path('deleteuser/', DeleteUser.as_view(), name='delete_user'),
]
