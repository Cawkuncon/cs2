from api_info.pagination import ListPagination, NoticePagination
from api_info.permissions import IsUsersNotice, IsAdminNotice
from api_info.serializator import SkinSerializer, NoticeSerializer, NoticeSerializerAdmin
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


class SkinDetailAdmin(generics.RetrieveUpdateDestroyAPIView):
    queryset = SkinInfo.objects.all()
    serializer_class = SkinSerializer
    permission_classes = [permissions.IsAdminUser, ]


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


class NoticeListAdmin(generics.ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializerAdmin
    pagination_class = NoticePagination
    permissions = [permissions.IsAdminUser, ]


class NoticeDetailAdmin(generics.RetrieveDestroyAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializerAdmin
    pagination_class = NoticePagination
    permissions = [IsAdminNotice, ]
