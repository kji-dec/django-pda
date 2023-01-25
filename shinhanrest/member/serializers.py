from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        request = self.context['request']
        if Member.objects.filter(username=request.data.get('username')).exists():
            return serializers.ValidationError('duplicated id.')
        return attrs
    
    def create(self, validated_data):
        member = Member.objects.create(
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            tel = validated_data['tel'],
        )
        member.save()

        return member
    
    class Meta:
        model = Member
        fields = '__all__'
        extra_kwargs = {"password": {"write_only": True}}
