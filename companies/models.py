from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=20, verbose_name='국가')

    class Meta:
        db_table = 'countries'


class Location(models.Model):
    name = models.CharField(max_length=20, verbose_name='지역')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = 'locations'


class Company(models.Model):
    name = models.CharField(max_length=20, verbose_name='회사명')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        db_table = 'companies'
