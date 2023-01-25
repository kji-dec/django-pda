from django.contrib.auth.hashers import make_password
from rest_framework import mixins, generics

from .serializers import MemberSerializer


class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):

    serializer_class = MemberSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)