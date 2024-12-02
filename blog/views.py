from rest_framework import viewsets, mixins
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from blog.models import UserProfile, Post, Comment
from blog.serializers import UserSerializer, CommentSerializer, UserProfileSerializer, PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = UserProfileSerializer

    def get_object(self):
        user_id = self.kwargs.get("userId")
        profile = get_object_or_404(UserProfile, user_id=user_id)
        return profile


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("post_pk")
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_pk")
        serializer.save(post_id=post_id)
