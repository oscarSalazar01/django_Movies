from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Pelicula, Pelicula_location


class PeliculaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = ('id', 'titulo', 'calificacion', 'pais')
        
    def to_representation(self, instance):
        return{
            'titulo': instance.titulo,
            'calificacion': instance.calificacion,
            'pais': instance.pais
        }

class Pelicula_locationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Pelicula_location
        geo_field = "point"
        fields = ('titulo', 'calificacion', 'pais')

