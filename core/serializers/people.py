from rest_framework.serializers import ModelSerializer

from core.models import People

class PeopleSerializer(ModelSerializer):
    class Meta:
        model = People
        fields = "__all__"