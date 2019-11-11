from rest_framework import serializers


class RunnerPythonSerializer(serializers.Serializer):
    cmd = serializers.CharField(max_length=8, min_length=5)
    code = serializers.CharField(max_length=99999)
