from rest_framework import serializers
from core.models import BuildNameModel, BuildModel


class BuildNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuildNameModel
        fields = ("__all__")


class BuildModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuildModel
        fiedls = ("__all__")