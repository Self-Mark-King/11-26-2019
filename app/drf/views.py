from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from drf.serializers import UserSerializer, GroupSerializer

class User_viewset(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer

class Group_Viewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

