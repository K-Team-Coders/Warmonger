from django.db import models
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(default=' ', max_length=100)
    
    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name

class Location(models.Model):
    name = models.CharField(default=' ', max_length=200)
    adress = models.CharField(default=' ', max_length=200)
    latitude = models.FloatField(default=1.0)
    longitude = models.FloatField(default=1.0)

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name

class Person(models.Model):
    name = models.CharField(default=' ', max_length=90)
    nickname = models.CharField(default=' ', max_length=90)

    def __repr__(self) -> str:
        return self.name
        
    def __str__(self) -> str:
        return self.name

class Organisation(models.Model):
    name = models.CharField(default=' ', max_length=90)
    site = models.URLField(default=' ')

    def __repr__(self) -> str:
        return self.name
        
    def __str__(self) -> str:
        return self.name

class News(models.Model):
    title = models.CharField(default=' ', max_length=50)
    text = models.TextField(default=' ', max_length=300)
    source = models.CharField(default=' ', max_length=70)
    date = models.DateField(default=timezone.now())

    locations = models.ManyToManyField(Location)
    persons = models.ManyToManyField(Person)
    organizations = models.ManyToManyField(Organisation)
    tags = models.ManyToManyField(Tag)

    def __repr__(self) -> str:
        return self.title        

    def __str__(self) -> str:
        return self.title
