from django.contrib import admin
from .models import Player, Quest, UserQuest
# Register your models here.
admin.site.register(Player)
admin.site.register(Quest)
admin.site.register(UserQuest)
