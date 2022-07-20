from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import CommentViewSet, PostViewSet, GroupViewSet, FollowViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
    path('v1/follow/', FollowViewSet.as_view(
        {'get': 'list', 'post': 'create'})
    ),
]
