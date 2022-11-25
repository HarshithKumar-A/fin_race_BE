# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Players, LeadBoard


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields =  "__all__"

class LeadBoardSerializer(serializers.ModelSerializer):
    # name = PlayerSerializer()
    player_name = serializers.SerializerMethodField('get_player_name')
    # id = serializers.IntegerField(source='name.id')
    class Meta:
        model = LeadBoard
        ordering = ('score', )
        fields = ('id', 'name','score','player_name')
        # write_only = ('name',)

    def get_player_name(self, obj):
        return obj.name.name

