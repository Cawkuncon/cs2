from django.urls import path
from api_info import views

urlpatterns = [
    path('skins/<int:pk>', views.SkinDetail.as_view(), name='api_skin_detail'),
    path('skins/', views.SkinList.as_view(), name='api_skins'),
    path('notices/<int:pk>/', views.NoticeDetail.as_view(), name='api_notice_detail'),
    path('notices/', views.NoticeList.as_view(), name='api_notices'),
]
