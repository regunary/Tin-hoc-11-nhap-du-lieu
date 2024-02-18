from django.contrib import admin
from .models import Musician, Song

# Register your models here.
@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'instrument')
    search_fields = ('first_name', 'last_name')

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'musician', 'release_date')
    search_fields = ('title', 'musician__first_name', 'musician__last_name')
    list_filter = ('release_date',)