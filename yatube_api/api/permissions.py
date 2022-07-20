from rest_framework.permissions import IsAuthenticated


class IsAuthorOrReadOnly(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
