from rest_framework import serializers
from core.models import NameModel, CNPJModel, BuildRegisterModel, BuildInfoModel


class NameSerializer(serializers.ModelSerializer):

    class Meta:
        model = NameModel
        fields = ("__all__")


class CNPJSerializer(serializers.ModelSerializer):

    class Meta:
        model = CNPJModel
        fields = ("__all__")


class BuildRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuildRegisterModel
        fiedls = ("__all__")


class BuildInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuildInfoModel
        fiedls = ("__all__")