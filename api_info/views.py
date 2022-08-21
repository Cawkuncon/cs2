from api_info.serializator import SkinSerializer, NoticeSerializer
from csinf.models import SkinInfo, Notice
from rest_framework import generics, permissions, pagination


class ListPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000


class SkinList(generics.ListAPIView):
    queryset = SkinInfo.objects.all()
    serializer_class = SkinSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    pagination_class = ListPagination


class SkinDetail(generics.RetrieveAPIView):
    queryset = SkinInfo.objects.all()
    serializer_class = SkinSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class NoticeList(generics.ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    pagination_class = [permissions.IsAuthenticated, ]
