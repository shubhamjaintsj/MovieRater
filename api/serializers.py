from rest_framework import serializers
from rest_framework.authtoken.models import Token
from . import models as api_models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.User
        fields = ['id','username', 'password']
        extra_kwargs = {'password': {'write_only':True, 'required': True}}

    def create(self, validated_data):
        user = api_models.User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Movie
        fields = ['id','title','description', 'no_of_rating', 'avg_rating']

class RaitingSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Raiting
        fields = ['id','movie','user', 'stars']