from django.contrib import admin
from .models import Concert, Venue, Band

# Register your models here.
admin.site.register(Concert)
admin.site.register(Venue)
admin.site.register(Band)
