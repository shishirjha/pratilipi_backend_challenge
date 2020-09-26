from rest_framework import serializers


class ResultSerializer(serializers.Serializer):
    readiness = serializers.CharField(read_only=True)
    validity = serializers.CharField(read_only=True)
