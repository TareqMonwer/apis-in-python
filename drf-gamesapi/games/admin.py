from django.contrib import admin
from games.models import Game, GameCategory


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'played', 'game_category')


@admin.register(GameCategory)
class GameCategoryAdmin(admin.ModelAdmin):
    pass