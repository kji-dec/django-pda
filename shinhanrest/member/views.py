from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import status, mixins, generics

from .models import Member
from .serializers import MemberSerializer


class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):

    serializer_class = MemberSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)