from django.shortcuts import render
from django.views.generic import TemplateView

# Models import 
from core.models import NameModel, CNPJModel, CondominiumInfoModel

# DRF / Serializers
from rest_framework import generics, permissions
from core.serializers import NameSerializer, CNPJSerializer, CondominiumInfoSerializer

# Land Page
class IndexView(TemplateView):
    template_name: str = "index.html"
    
    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx["name"] = NameModel.objects.all()
        return ctx


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


class CondominiumInfoAPI(generics.ListAPIView):
    serializer_class = CondominiumInfoSerializer
    queryset = CondominiumInfoModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class CondominiumInfoSearchAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CondominiumInfoSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = CondominiumInfoModel.objects.all()
            filter_search = self.request.GET.get('id', None)
            if filter_search is not None:
                queryset = queryset.filter(id=filter_search)
            return queryset