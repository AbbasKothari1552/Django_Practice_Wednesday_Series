from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Venue)

# customizing the admin panel
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):

    list_display = ('name', 'address', 'phone_no')
    ordering = ('name',)
    search_fields = ('name', 'address', 'phone_no')
