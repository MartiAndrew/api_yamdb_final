from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user.models import User
from user.consts import SERVICE_NAME


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")

    def validate_username(self, value):
        if value == SERVICE_NAME:
            raise ValidationError(
                f"Использовать {SERVICE_NAME} в качестве username запрещено."
            )

        return value


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        fields = ("username", "confirmation_code")
