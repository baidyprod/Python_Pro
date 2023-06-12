from blog_api.models import Comment, Publication
from blog_api.permissions import IsOwnerOrReadOnly
from blog_api.serializers import CommentSerializer, PublicationSerializer

from django.contrib.auth import get_user_model

from rest_framework import permissions, viewsets


User = get_user_model()


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all().order_by('-created_at')
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
