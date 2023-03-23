from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.services import get_tokens_for_user, send_confimation_code_on_email

from .serializers import SignUpSerializer, TokenSerializer


class SignUpAPIView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=SignUpSerializer)
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = User.objects.get(email=request.data["email"])

        send_confimation_code_on_email(user)

        return Response(serializer.data)


class TokenAPIView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=TokenSerializer())
    def post(self, request):
        serializer = TokenSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, username=request.data["username"])
        if not default_token_generator.check_token(
            user,
            serializer.data["confirmation_code"],
        ):
            raise ValidationError("Неверный код")

        token = get_tokens_for_user(user)

        return Response(token)
