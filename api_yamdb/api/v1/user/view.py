from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User

from .permissions import AdminPermission
from .serializers import UserPatchSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AdminPermission,)
    filter_backends = (SearchFilter,)
    search_fields = ('username',)
    http_method_names = ['get', 'post', 'patch', 'delete']
    lookup_field = 'username'


class UserMeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UserPatchSerializer)
    def patch(self, request):
        serializer = UserPatchSerializer(
            request.user,
            data=request.data,
            partial=True,
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
