from django.contrib.auth.tokens import default_token_generator
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.core.mail import send_mail


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    access_token = str(refresh.access_token)

    return dict(token=access_token)


def generate_confirmation_code(user):
    return default_token_generator.make_token(user)


def send_confimation_code_on_email(user):
    send_mail(
        "Поздравляем с успешной регистрацией!",
        f"Ваш код подтверждения: {generate_confirmation_code(user)}",
        settings.SERVICE_EMAIL,
        [user.email],
    )
