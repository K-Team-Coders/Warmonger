from rest_framework import serializers

from .models import *

class personSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class organizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class newsSerializer(serializers.ModelSerializer):
    tags = tagSerializer(many=True)
    locations = locationSerializer(many=True)
    persons = personSerializer(many=True)
    organizations = organizationSerializer(many=True)

    class Meta:
        model = News
        fields = '__all__'

