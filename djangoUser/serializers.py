from rest_framework import serializers
from .models import extendedUser

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=extendedUser
        fields=['email','password','age','address','gender','username','first_name','last_name']