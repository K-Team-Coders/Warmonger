from django.http import HttpResponse, JsonResponse
from django.core.files.storage import default_storage    
from django.core.files.base import ContentFile
from django.conf import settings

from rest_framework.views import APIView

from .apps import MainConfig

import numpy as np
from loguru import logger
import random

class uploadfile(APIView):

    def post(self, request):
        path = 0
        file_objs = request.data.getlist('file')
        for file_obj in file_objs:
            path = os.path.join(settings.CSV_ROOT, file_obj.name)
            logger.debug(path)
            default_storage.save(path, ContentFile(file_obj.read())) 

        return JsonResponse({
            'from': 'ready_joins',
        })

class modelInterface(APIView):

    def post(self, request):
        prediction = MainConfig.some_model.predict(request.PAYLOAD)
        return prediction

class testdata(APIView):

    def get(self, request):
        array_X = [(x + random.uniform(1.2, 20.0)) for x in range(50)]
        array_Y = [(x + random.uniform(1.2, 20.0)) for x in range(50)]

        logger.debug((array_X, array_Y))
        logger.debug(list(zip(array_X, array_Y)))

        return JsonResponse({
            'x':array_X,
            'y':array_Y,
            'pack': list(zip(array_X, array_Y))
        })

class testdata_barchart(APIView):

    def get(self, request):
        array_X = [(x + random.uniform(1.2, 20.0)) for x in range(100)]
        array_Y = [(x + random.uniform(1.2, 20.0)) for x in range(100)]

        logger.debug((array_X, array_Y))
        logger.debug(list(zip(array_X, array_Y)))

        return JsonResponse({
            'x':array_X,
            'labels':array_Y,
        })

class testdata_radarchart(APIView):

    def get(self, request):
        array_X = [(x + random.uniform(1.2, 20.0)) for x in range(10)]
        array_Y = [x for x in range(10)]

        logger.debug((array_X, array_Y))

        return JsonResponse({
            'x':array_X,
            'labels':array_Y,
        })
        