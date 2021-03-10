from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import permissions
from web_api.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from web_api.paginations import StandardResultsSetPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class UserList(generics.ListAPIView):
    
    #queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend]
    search_fields = ['username', 'email','first_name']
    filterset_fields = ['is_active', ]
    ordering_fields = ['id','username', 'email']

    def get_queryset(self):

        # queryset
        queryset = User.objects.all()

        # qrery string
        group = self.request.GET.get("group",None)

        # filter
        if group is not None:
            queryset = queryset.filter(groups__name=group)

        return queryset