from django.db import IntegrityError
from rest_framework import serializers
from .models import Likes


class LikesSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Likes
        fields = [
            'id', 'owner', 'post', 'created_at'
        ]

    def create(self, validate_data):
        try:
            return super().create(validate_data)
        except IntegrityError:
            raise serializers.ValidateError({
                'detail': 'possible duplicate'
            })
