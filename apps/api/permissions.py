from rest_framework import permissions


class IsAdministratorOrViewer(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        is_admin_or_viewer = user.groups.filter(name__in=['Viewer', 'Administrator']).exists()

        return is_admin_or_viewer


class IsAdministratorOrViewerForGET(permissions.BasePermission):
    def has_permission(self, request, view):        
        
        if request.method == 'GET':
            user = request.user

            is_admin_or_viewer = user.groups.filter(name__in=['Viewer', 'Administrator']).exists()
            return is_admin_or_viewer
            
        return False

class IsAdministratorForPatch(permissions.BasePermission):
    def has_permission(self, request, view):        

        if request.method == 'PATCH':
            user = request.user

            is_admin = user.groups.filter(name__in=['Administrator']).exists()
            return is_admin
            
        return False