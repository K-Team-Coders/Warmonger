import json
import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ReadOnlyModelViewSet

from collections import Counter
from loguru import logger

from .models import *
from .serializers import *

class getAllNews(ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = newsSerializer
    
class getAllTags(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = tagSerializer

class getDetailedNews(APIView):
    
    def get(self, request, pk):
        objects = News.objects.filter(pk=pk)
        seri = newsSerializer(objects, many=True)
        data = seri.data
        return Response(data)

class topNews(APIView):
    def get(self, request):
        news = News.objects.all()
        seria = newsSerializer(news, many=True)
        data = seria.data

        tags = []
        persons = []
        organizations = []
        locations = []

        for subdata in data:
            tags.extend([tag['name'] for tag in subdata['tags']])
            persons.extend([tag['name'] for tag in subdata['persons']])
            organizations.extend([tag['name'] for tag in subdata['organizations']])
            locations.extend([tag['name'] for tag in subdata['locations']])

        tags = Counter(tags).most_common(5)
        organizations = Counter(organizations).most_common(5)
        persons = Counter(persons).most_common(5)
        locations = Counter(locations).most_common(5)
        
        tag_labels = []
        tag_count = []
        for tuple_ in tags:
            tag_labels.append(tuple_[0])
            tag_count.append(tuple_[1])

        organizations_labels = []
        organizations_count = []
        for tuple_ in organizations:
            organizations_labels.append(tuple_[0])
            organizations_count.append(tuple_[1])

        persons_labels = []
        persons_count = []
        for tuple_ in persons:
            persons_labels.append(tuple_[0])
            persons_count.append(tuple_[1])

        locations_labels = []
        locations_count = []
        for tuple_ in locations:
            locations_labels.append(tuple_[0])
            locations_count.append(tuple_[1])

        return JsonResponse(data={
            'tag_labels': tag_labels,
            'tag_count': tag_count,
            'organizations_labels': organizations_labels,
            'organizations_count': organizations_count,
            'persons_labels': persons_labels,
            'persons_count': persons_count,
            'locations_label': locations_labels,
            'location_count': locations_count
        })

class relationNews(APIView):

    def get(self, request):
        objects = News.objects.all()
        seria = newsSerializer(objects, many=True)
        data = seria.data
        
        node = []

        for subdata in data:
            node.append({"name": subdata['title']})

            for tag in subdata['tags']:
                node.append({"name": tag['name']})
            
            for person in subdata['persons']:
                node.append({'name': person['name']})

            for org in subdata['organizations']:
                node.append({"name": org['name']})

            for loc in subdata['locations']:
                node.append({"name": loc['name']})

        names = []
        uniques = []

        for item in node:
            if item['name'] not in names:
                names.append(item['name'])
                uniques.append(item)

        relations = []

        for subdata in data:
            current_source = names.index(subdata['title'])
            logger.debug(current_source)


            for tag in subdata['tags']:
                current_destenation = names.index(tag['name'])
                relations.append({
                    'source': current_source,
                    'target': current_destenation,
                    'relation': 'TAG',
                    'value': 20
                })
            for person in subdata['persons']:
                current_destenation = names.index(person['name'])
                relations.append({
                    'source': current_source,
                    'target': current_destenation,
                    'relation': 'PER',
                    'value': 20
                })

            for org in subdata['organizations']:
                current_destenation = names.index(org['name'])
                relations.append({
                    'source': current_source,
                    'target': current_destenation,
                    'relation': 'ORG',
                    'value': 20
                })

            for loc in subdata['locations']:
                current_destenation = names.index(loc['name'])
                relations.append({
                    'source': current_source,
                    'target': current_destenation,
                    'relation': 'LOC',
                    'value': 20
                })
        
        return JsonResponse({
            'nodes': uniques, 
            'relations': relations
            })

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
            organizationObject, isCreated = Organization.objects.get_or_create(
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