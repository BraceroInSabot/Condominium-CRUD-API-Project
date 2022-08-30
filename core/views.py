from django.shortcuts import render
from django.views.generic import TemplateView

# Models import 
from core.models import NameModel, CNPJModel, BuildRegisterModel, BuildInfoModel

# DRF / Serializers
from rest_framework import generics, permissions
from core.serializers import NameSerializer, CNPJSerializer, BuildRegisterSerializer, BuildInfoSerializer

# Land Page
class IndexView(TemplateView):
    template_name: str = "index.html"

# Customizable APIS for admins
class NameAPI(generics.ListAPIView):
    serializer_class = NameSerializer
    queryset = NameModel.objects.all()


class NameSearchAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NameSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = NameModel.objects.all()
            filter_search = self.request.GET.get('id', None)
            if filter_search is not None:
                queryset = queryset.filter(id=filter_search)
            return queryset

class CNPJAPI(generics.ListAPIView):
    serializer_class = CNPJSerializer
    queryset = CNPJModel.objects.all()


class CNPJSearchAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CNPJSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = CNPJModel.objects.all()
            filter_search = self.request.GET.get('id', None)
            if filter_search is not None:
                queryset = queryset.filter(id=filter_search)
            return queryset


class BuildRegisterAPI(generics.ListAPIView):
    serializer_class = BuildRegisterSerializer
    queryset = BuildRegisterModel.objects.all()


class BuildRegisterSearchAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BuildRegisterSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = BuildRegisterModel.objects.all()
            filter_search = self.request.GET.get('id', None)
            if filter_search is not None:
                queryset = queryset.filter(id=filter_search)
            return queryset


class BuildInfoAPI(generics.ListAPIView):
    serializer_class = BuildInfoSerializer
    queryset = BuildInfoModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class BuildInfoSearchAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BuildInfoSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = BuildInfoModel.objects.all()
            filter_search = self.request.GET.get('id', None)
            if filter_search is not None:
                queryset = queryset.filter(id=filter_search)
            return queryset