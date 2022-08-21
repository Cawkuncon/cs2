from rest_framework import permissions


class IsUsersNotice(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.username_notice:
            return True
