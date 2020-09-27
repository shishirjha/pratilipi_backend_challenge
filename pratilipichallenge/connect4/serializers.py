from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):

    column = serializers.IntegerField()

    def get_column(self, obj):
        return obj.get_column()

    class Meta:
        model = Game
        fields = ('column', 'player')
        read_only_fields = ('validity',)