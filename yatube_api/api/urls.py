from django.urls import path, include

from rest_framework.authtoken import views

from rest_framework.routers import SimpleRouter

from .views import GroupViewSet, PostViewSet, CommentViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet, basename='groups')

comments_router = SimpleRouter()
comments_router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/posts/<int:post_id>/', include(comments_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
