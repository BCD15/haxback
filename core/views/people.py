from rest_framework.viewsets import ModelViewSet

from core.models import People
from core.serializers import PeopleSerializer

class PeopleViewSet(ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer