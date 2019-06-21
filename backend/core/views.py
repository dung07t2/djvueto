from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import viewsets, filters

from core_auth.serializers import GroupSerializer
from .serializers import UserSerializer, RecipeSerializer
from .models import Recipe

UserModel = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email', 'first_name')


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()