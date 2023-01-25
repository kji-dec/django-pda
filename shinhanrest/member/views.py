from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import status

from .models import Member


class MemberRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        tel = request.data.get('tel')

        if Member.objects.filter(username=username).exists():
            message = {
                'detail': "duplicated id",
            }
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        member = Member(
            username = username,
            password = make_password(password),
            tel = tel,
        )

        member.save()

        return Response(status=status.HTTP_201_CREATED)