from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    groups = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups','first_name']
    
    def get_groups(self,obje):
        groups = obje.groups.values_list('name',flat = True) # QuerySet Object
        return list(groups)
