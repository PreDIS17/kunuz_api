from django.contrib import admin

from common import models

admin.site.register(models.ContactCreate)
admin.site.register(models.Advertisement)
admin.site.register(models.NewsTag)
admin.site.register(models.NewsCategory)
admin.site.register(models.Region)
admin.site.register(models.News)
