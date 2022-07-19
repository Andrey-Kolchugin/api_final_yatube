# TODO:  Напишите свой вариант
from posts.models import Post
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from .serializers import PostSerializer


# from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)