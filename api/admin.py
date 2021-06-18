from django.contrib import admin
from . import models as api_models

admin.site.register(api_models.Movie)
admin.site.register(api_models.Raiting)
