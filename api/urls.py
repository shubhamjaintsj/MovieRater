from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views as api_views

router = routers.DefaultRouter()
router.register('movies', api_views.MovieViewSets)
router.register('ratings', api_views.RaitingViewSets)
router.register('users', api_views.UserViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
