from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)

    def is_valid(self, raise_exception=False):
        return super().is_valid(raise_exception=raise_exception)
    
    