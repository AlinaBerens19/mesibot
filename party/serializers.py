from rest_framework import serializers

from .models import Party


class PartySerializer(serializers.ModelSerializer):

    image = serializers.ImageField(required=False)

    class Meta:
        model = Party
        fields = '__all__'
        





