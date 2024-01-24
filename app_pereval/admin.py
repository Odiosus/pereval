from django.contrib import admin

from .models import AppUser, Coords, Level, Pereval, Images

admin.site.register(AppUser)
admin.site.register(Coords)
admin.site.register(Level)
admin.site.register(Pereval)
admin.site.register(Images)
