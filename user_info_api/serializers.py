from rest_framework import serializers
from .models import userInfo


class userInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = userInfo
        # fields = "__all__"
        fields = ['name', 'phoneNo', 'age', 'address', 'email']
