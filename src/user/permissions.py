from rest_framework.permissions import BasePermission




class UserPermission(BasePermission):



    def has_permission(self, request, view):

        if request.user.is_authenticated() and view.action in ("retrieve", "update", "destroy"):
            return True

        if request.user.is_superuser and view.action == "list":
            return True

        #cualquiera puede crear un usuario
        if view.action == "create":
            return True

        return False


    def has_object_permission(self, request, view, obj):

        return request.user.is_superuser or request.user == obj