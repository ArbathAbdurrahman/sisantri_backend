from rest_framework import permissions

class IsOwnerOfProfile(permissions.BasePermission):
    """
    Permission untuk hanya mengizinkan pemilik profil untuk mengeditnya.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user