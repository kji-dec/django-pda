from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    #lecturer's code
    def validate_password(self, value):
        # validation이 끝난 value를 반환해줌
        if len(value) < 8:
            raise serializers.ValidationError('Too short password')
        return make_password(value)
    # my code
    # def create(self, validated_data):
    #     member = Member.objects.create(
    #         username=validated_data['username'],
    #         password=make_password(validated_data['password']),
    #         tel = validated_data['tel'],
    #     )
    #     member.save()

    #     return member

    # def validate(self, attrs):
    #     if len(attrs['password']) < 8:
    #         raise serializers.ValidationError('Too short password')
        
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError('different password')
        
    #     attrs['password'] = make_password(attrs['password'])
    #     return attrs
    
    class Meta:
        model = Member
        fields = ('id', 'username', 'tel', 'password') # don't forget id field!
        extra_kwargs = {
            "id":{
                "read_only": True,
            },
            "password": {
                "write_only": True,
            },
        }
