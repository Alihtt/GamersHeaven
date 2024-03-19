from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = 'Permission denied, you are not the owner of this article'

    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS:
            return request.user.is_authenticated and request.user
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.author
