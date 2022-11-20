# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Players, LeadBoard



class LeadBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadBoard
        fields = ('name','score')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields =  "__all__"
