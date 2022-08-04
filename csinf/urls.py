from django.urls import path

from csinf import views

urlpatterns = [
    path('', views.skins, name='main'),
    path('goods/', views.ListSkins.as_view(), name='goods'),
    path('goods/<int:pk>/', views.SkinDetail.as_view(), name='skin_detail'),
    path('profileskins/', views.ProfileListSkins.as_view(), name='profile_skins'),
    path('profiletable/', views.ProfileTableSkins.as_view(), name='profile_table'),
    path('notice/', views.NoticeSkins.as_view(), name='notice'),
    path('notice/<int:pk>/', views.NoticeSkinDetail.as_view(), name='notice_detail'),
]
