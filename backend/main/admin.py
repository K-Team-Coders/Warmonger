from django.contrib import admin
from .models import *

admin.site.register(News)
admin.site.register(Person)
admin.site.register(Organization)
admin.site.register(Location)
admin.site.register(Tag)