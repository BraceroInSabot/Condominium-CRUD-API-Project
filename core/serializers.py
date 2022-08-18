from rest_framework import serializers
from core.models import BuildNameModel, BuildCNPJModel, BuildModel


class BuildNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuildNameModel
        fields = ("__all__")


class BuildCNPJSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuildCNPJModel
        fields = ("__all__")

class BuildModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuildModel
        fiedls = ("__all__")