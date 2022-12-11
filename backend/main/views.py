import json
import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from loguru import logger

from .models import *

class detailedNewsView(APIView):
    def get(self, request, pk):
        data = get_object_or_404(News, pk=pk)
        logger.debug(data.id)
        return HttpResponse(status=200)

class addNew(APIView):
    def post(self, request):

        def personsDB(name = ' ', nickname = ' '):
            logger.debug(name)
            logger.debug(nickname)

            personObject, isCreated = Person.objects.get_or_create(
                name = name,
                nickname = nickname
            )

            if isCreated:
                personObject.save()

            return personObject

        def organizationsDB(name = ' ', site = ' '):
            logger.debug(name)
            logger.debug(site)
            organizationObject, isCreated = Organisation.objects.get_or_create(
                name = name,
                site = site
            )

            if isCreated:
                organizationObject.save()

            return organizationObject

        def locationDB(name, adress, longitude, latitude):
            logger.debug(name)
            logger.debug(adress)
            logger.debug(longitude)
            logger.debug(latitude)
            locationObject, isCreated = Location.objects.get_or_create(
                name = name,
                adress = adress,
                latitude = latitude,
                longitude = longitude
            )

            if isCreated:
                locationObject.save()

            return locationObject
        
        def tagsDB(keyword):
            logger.debug(keyword)

            tagObject, isCreated = Tag.objects.get_or_create(
                name = keyword
            )

            if isCreated:
                tagObject.save()

            return tagObject

        data = json.loads(request.body)

        # Анализ организаций в процессе
        organizations = data['organizations']
        organizationObjects = []
        if organizations:
            organizationObjects = [organizationsDB(organization['name'], organization['site']) for organization in organizations]
        logger.success(organizationObjects)

        persons = data['persons']
        personObjects = []
        if persons:
            personObjects = [personsDB(person['name'], person['nickname']) for person in persons]
        logger.success(personObjects)
        
        keywords = data['keywords']

        # Данные в объекты по локациям
        locations = data['locations']
        locationObjects = [locationDB(location['name'], location['adress'], float(location['longitude']), float(location['latitude'])) for location in locations]
        logger.success(locationObjects)

        # Ключевые слова,помогающие понять о чем говорят в новости
        tags = []
        tags.extend(keywords)
        tags.extend([organization['name'] for organization in organizations])
        tags.extend([person['name'] for person in persons])

        tagObjects = [tagsDB(tag) for tag in tags]
        logger.success(tagObjects)

        title =  data['title']
        text = data['text']
        date  = datetime.datetime.strptime(data['date'][:len(data['date']) - 6], '%Y-%m-%d %H:%M:%S')
        source = data['source']
        
        newsObject, isCreated = News.objects.get_or_create(
            title = title,
            text = text,
            date = date,
            source = source,
        )
        logger.success(newsObject)
        if isCreated:
            newsObject.save()
            if personObjects:
                for obj in personObjects:
                    newsObject.persons.add(obj)
            if organizationObjects:
                for obj in organizationObjects:
                    newsObject.organisations.add(obj)
            if tagObjects:
                for obj in tagObjects:
                    newsObject.tags.add(obj)
            if locationObjects:
                for obj in locationObjects:
                    newsObject.locations.add(obj)
            
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=200)