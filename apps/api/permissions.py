from rest_framework import permissions


class IsAdministratorOrViewer(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        is_admin_or_viewer = user.groups.filter(
            name__in=['Viewer', 'Administrator']).exists()

        return is_admin_or_viewer


class IsAdministratorOrViewerForGET(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method == 'GET':
            user = request.user

            is_admin_or_viewer = user.groups.filter(
                name__in=['Viewer', 'Administrator']).exists()
            return is_admin_or_viewer

        return False


class IsAdministratorForPatch(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method == 'PATCH':
            user = request.user

            is_admin = user.groups.filter(name__in=['Administrator']).exists()

            return is_admin

        return False


class AllowAnyForGET(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method == 'GET':
            return True

        return False


class IsAdminOrSameRequestUserForPATCH(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if request.method == 'PATCH':

            pk_user_to_delete = request.resolver_match.kwargs.get('pk')
            request_user_pk = user.organization_member.pk

            return pk_user_to_delete == request_user_pk or \
                user.groups.filter(name__in=['Administrator']).exists()

        return False


class isAdminForDELETE(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method == 'DELETE':
            user = request.user

            return user.groups.filter(name__in=['Administrator']).exists()

        return False

        i


class IsAdministratorOrViewerForGET(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if request.method == 'GET':
            is_admin_or_viewer = user.groups.filter(
                name__in=['Viewer', 'Administrator']).exists()

            return is_admin_or_viewer
        
        return False


class IsAdministratorForPOST(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if request.method == 'POST':
            is_admin = user.groups.filter(
                name__in=['Administrator']).exists()

            return is_admin
        
        return False