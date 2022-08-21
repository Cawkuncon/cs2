from rest_framework import permissions


class IsUsersNotice(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.username_notice:
            return True


class IsAdminNotice(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff and request.method in ('GET', 'HEAD', 'OPTIONS', 'DELETE'):
            return True
