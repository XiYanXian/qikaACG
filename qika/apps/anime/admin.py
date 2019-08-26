from django.contrib import admin
from .models import  Character, Staff, Supervision, AnimeList, VoiceActor, AnimeTimeWeek, Musician
# Register your models here.
admin.site.register(Character)
admin.site.register(Staff)
admin.site.register(Supervision)
admin.site.register(AnimeList)
admin.site.register(VoiceActor)
admin.site.register(AnimeTimeWeek)
admin.site.register(Musician)
