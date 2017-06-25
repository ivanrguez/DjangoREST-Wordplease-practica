from rest_framework.permissions import BasePermission




class TasksPermission(BasePermission):



    def has_permission(self, request, view):

        if request.user.is_authenticated() or request.user.is_superuser and view.action in ("retrieve", "create", "update", "destroy"):
            return True


        #cualquiera puede ver post
        if view.action == "list":
            return True

        return False


    def has_object_permission(self, request, view, obj):

        return request.user.is_superuser or request.user == obj.post.user