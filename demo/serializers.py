from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from demo.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'rating']

    def validate_author(self, value):
        if 'client' in value:
            raise ValidationError('incorrect author')
        print(value)
        return value
