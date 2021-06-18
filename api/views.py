from django.shortcuts import render
from rest_framework import response
from . import models as api_models, serializers as api_serializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

class UserViewSets(viewsets.ModelViewSet):
    queryset = api_models.User.objects.all()
    serializer_class = api_serializers.UserSerializer

class MovieViewSets(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = api_models.Movie.objects.all()
    serializer_class = api_serializers.MovieSerializer

    @action(detail=True, methods=['POST'])
    def rate_movie(self,request, pk):
        result = {}
        message = ''
        error_message = ''
        _status = ''
        if not request.data.get('stars'):
            error_message = 'you need to provide stars'
            _status = status.HTTP_400_BAD_REQUEST

        stars = request.data['stars']

        try:
            stars = int(stars)
        except:
            error_message = 'stars must be integer'
            _status = status.HTTP_400_BAD_REQUEST

        if not error_message:

            # user = api_models.User.objects.get(id=2)
            user = request.user
            movie = api_models.Movie.objects.get(id=pk)


            try:
                rating = api_models.Raiting.objects.get(
                    user=user.id,
                    movie=movie.id
                )
                rating.stars = stars
                rating.save()
                message = 'Rating updated'
            except api_models.Raiting.DoesNotExist:
                rating = api_models.Raiting.objects.create(
                    user=user,
                    movie=movie,
                    stars = stars
                )
                message = 'Rating created'

            _status = status.HTTP_200_OK
            result = api_serializers.RaitingSerializer(rating,many=False).data

        response = {
            'error_message': error_message,
            'message': message,
            'result': result
        }

        return Response(response, status=_status)

class RaitingViewSets(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = api_models.Raiting.objects.all()
    serializer_class = api_serializers.RaitingSerializer

    def create(self, request, *args, **kwargs):
        response = {'message': "You can't update this"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        response = {'message': "You can't update this"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)