from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request,view,obj):
        if obj.user:
            return obj.user == request.user
        return False