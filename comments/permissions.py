from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user # True/False, 이거에 대한 Permission이 있냐 없냐 판단해준다. 기존 것을 override 한