from rest_framework import serializers
from .models import JobPost
from companies.serializers import CompanySerializer


class JobPostSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company_id.name', read_only=True)
    country = serializers.CharField(source='company_id.location.country.name', read_only=True)
    location = serializers.CharField(source='company_id.location.name', read_only=True)

    class Meta:
        model = JobPost
        fields = (
            'id',
            'position',
            'reward',
            'tech_stack',
            'contents',
            'company',
            'location',
            'country',
        )
        read_only_fields = (
            'company',
            'location',
            'country',
        )