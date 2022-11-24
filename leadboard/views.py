from django.shortcuts import render
from rest_framework import viewsets
from .models import LeadBoard, Players
from .serializer import LeadBoardSerializer, PlayerSerializer
# Create your views here.

class LeadboardView(viewsets.ModelViewSet):
    queryset = LeadBoard.objects.order_by('-score').all()
    serializer_class = LeadBoardSerializer


class PlayerView(viewsets.ModelViewSet):
    queryset = Players.objects.all()
    serializer_class = PlayerSerializer


