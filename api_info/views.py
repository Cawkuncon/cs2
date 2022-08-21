from api_info.pagination import ListPagination, NoticePagination
from api_info.permissions import IsUsersNotice
from api_info.serializator import SkinSerializer, NoticeSerializer
from csinf.models import SkinInfo, Notice
from rest_framework import generics, permissions


class SkinList(generics.ListAPIView):
    queryset = SkinInfo.objects.all()
    serializer_class = SkinSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    pagination_class = ListPagination


class SkinDetail(generics.RetrieveAPIView):
    queryset = SkinInfo.objects.all()
    serializer_class = SkinSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class NoticeList(generics.ListCreateAPIView):
    serializer_class = NoticeSerializer
    permissions = [permissions.IsAuthenticated, ]
    pagination_class = NoticePagination

    def get_queryset(self):
        user = self.request.user
        return Notice.objects.filter(username_notice=user)


class NoticeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notice.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsUsersNotice]
    serializer_class = NoticeSerializer
