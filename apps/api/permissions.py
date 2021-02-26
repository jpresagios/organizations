from rest_framework import permissions


class IsAdministratorOrViewer(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        is_admin_or_viewer = user.groups.filter(name__in=['Viewer', 'Administrator']).exists()

        return is_admin_or_viewer
