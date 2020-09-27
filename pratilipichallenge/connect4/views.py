from django.shortcuts import render
import connect4
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GameSerializer
from rest_framework import status
from .models import Game
# Create your views here.


class GamePlayApiView(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = GameSerializer

    def get_queryset(self):
        queryset = Game.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            game_instance = Game.objects.create()
            board, validity = game_instance.make_move(
                player=request.data['player'], col=request.data['column'])

        response = Response({"validity": validity}, status=status.HTTP_200_OK)
        return response


# class GameStartAPIView(APIView):
#     permission_classes = [
#         permissions.AllowAny,
#     ]
#     if request.data['game_status'] == "START":
#         return Response("READY")
