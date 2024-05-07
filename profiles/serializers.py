from rest_framework import serializers
from .models import Profile



class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Profile
        fields = [
            'owner',
            'created_at',
            'updated_at',
            'name',
            'content',
            'image',
            'id',
        ]
        read_only_fields = ['created_at', 'updated_at']