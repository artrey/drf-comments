from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from demo.models import Comment
from demo.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_fields = ['rating', 'author']
    search_fields = ['text', 'author']
    ordering_fields = ['author', 'rating']
    pagination_class = PageNumberPagination
