from rest_framework import routers
from .api import PeliculaViewSet, PeliculaSearchViewSet, Pelicula_locationViewSet

router = routers.DefaultRouter()

router.register('api/movies', PeliculaViewSet, 'movies')
router.register('api/search', PeliculaSearchViewSet, 'search')
router.register('api/geojson', Pelicula_locationViewSet, 'geojson')



urlpatterns = router.urls