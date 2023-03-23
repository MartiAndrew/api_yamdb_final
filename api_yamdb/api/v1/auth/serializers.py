from django.db.utils import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from user.consts import SERVICE_NAME
from user.models import User


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.RegexField(
        required=True,
        max_length=150,
        regex=r'^[\w.@+-]+',
    )
    email = serializers.EmailField(required=True, max_length=150)

    class Meta:
        model = User
        fields = ('username', 'email')

    def create(self, validated_data):
        try:
            user = User.objects.get_or_create(**validated_data)[0]
        except IntegrityError:
            raise ValidationError(
                'Отсутствует обязательное поле или оно некоректно',
            )
        return user

    def validate_username(self, value):
        if value.lower() == SERVICE_NAME:
            raise ValidationError(
                f'Использовать {SERVICE_NAME} в качестве username запрещено.',
            )

        return value


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        fields = ('username', 'confirmation_code')
