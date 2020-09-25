from django.contrib import admin

# import your models here
from .models import Platform, Game, Controller, Photo

# Register your models here
admin.site.register(Platform)
admin.site.register(Game)
admin.site.register(Controller)
admin.site.register(Photo)