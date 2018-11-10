from rest_framework import viewsets, routers
from app.models import Apikey
from app.serializer import ApikeySerializer

class ApikeyViewSet(viewsets.ModelViewSet):
    queryset = queryset = Apikey.objects.all()
    serializer_class = ApikeySerializer

router = routers.DefaultRouter()
router.register(r'apikeys', ApikeyViewSet)
