from django.apps import AppConfig
import tensorflow as tf
from tensorflow import keras
from django.conf import settings
from loguru import logger
import pandas as pd
import pickle as pkl
import os

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    # operators_count_skolkovo_regressor = 0
    # with open(os.path.join(settings.MODELS_ROOT, 'model.h5'), 'rb') as f:
    #     operators_count_skolkovo_regressor = pkl.load(f)
