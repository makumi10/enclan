from rest_framework import viewsets, permissions

from .models import BlogPost
from .serializers import BlogPostSerializer
from .permissions import IsOwnerOrReadOnly


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # set the author from the logged in user, don't trust the request body
        serializer.save(author=self.request.user)
