from rest_framework import serializers
from .models import Country, Location, Company


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model=Country
        fields ='__all__'


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model=Location
        fields ='__all__'


class CompanySerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True, read_only=True)
    location = LocationSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = (
            'name',
            'location',
            'country',
        )