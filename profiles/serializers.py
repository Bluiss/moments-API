from rest_framework import serializers
from .models import Profile



class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.owner


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
            'is_owner',
        ]
        read_only_fields = ['created_at', 'updated_at']