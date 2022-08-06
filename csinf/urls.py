from django.urls import path

from csinf import views

urlpatterns = [
    path('', views.skins, name='main'),
    path('goods/', views.ListSkins.as_view(), name='goods'),
    path('goods/<int:pk>/', views.SkinDetail.as_view(), name='skin_detail'),
    path('profileskins/', views.ProfileListSkins.as_view(), name='profile_skins'),
    path('profiletable/', views.ProfileTableSkins.as_view(), name='profile_table'),
    path('notices/', views.NoticeView.as_view(), name='notices'),
]
