from django.urls import path, include
from api_info import views

urlpatterns = [
    path('skins/<int:pk>/', views.SkinDetail.as_view(), name='api_skin_detail'),
    path('skins/admin/<int:pk>/', views.SkinDetailAdmin.as_view(), name='api_skin_detail_admin'),
    path('skins/', views.SkinList.as_view(), name='api_skins'),
    path('notices/<int:pk>/', views.NoticeDetail.as_view(), name='api_notice_detail'),
    path('notices/', views.NoticeList.as_view(), name='api_notices'),
    path('notices/admin/<int:pk>/', views.NoticeDetailAdmin.as_view(), name='api_notice_detail_admin'),
    path('notices/admin/', views.NoticeListAdmin.as_view(), name='api_notices_admin'),
    path('auth/', include('rest_framework.urls')),
]
