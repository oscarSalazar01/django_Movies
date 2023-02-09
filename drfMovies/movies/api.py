from .models import Pelicula, Pelicula_location
from rest_framework import viewsets, permissions, filters
from .serializers import PeliculaSerializers, Pelicula_locationSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PeliculaSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo', 'calificacion', 'pais']
    ordering_fields = ['titulo', 'calificacion', 'pais']

    filterset_fields = {
        'titulo': ['exact'],
        'calificacion': ['exact'],
        'pais': ['exact'],
    }

class PeliculaSearchViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PeliculaSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo', 'calificacion', 'pais']
    filterset_fields = {
        'titulo': ['exact'],
        'calificacion': ['exact'],
        'pais': ['exact'],
    }

class Pelicula_locationViewSet(viewsets.ModelViewSet):
    queryset = Pelicula_location.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Pelicula_locationSerializer


