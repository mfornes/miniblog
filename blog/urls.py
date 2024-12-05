from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from blog.views import LDAPAuthViewSet, UserViewSet, ProfileViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'ldap', LDAPAuthViewSet, basename='ldap-auth')

posts_router = NestedSimpleRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

profile_detail = ProfileViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'update',
})

urlpatterns = [
    path('', include(router.urls)),
    path("", include(posts_router.urls)),
    path("users/<int:userId>/profile", profile_detail, name="user-profile"),
]
