from django.contrib import admin
from django.utils.html import format_html
from .models import Team,GamePosition,Coach,Player

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=('name','bandera','escudo')

    def bandera(self,obj):
        return format_html('<img src={} width=100 height=100 />',obj.flag.url)
    def escudo(self,obj):
        return format_html('<img src={} width=100 height=100 />',obj.shield.url)

@admin.register(GamePosition)
class GamePosition(admin.ModelAdmin):
    list_display=('name','description')

@admin.register(Coach)
class Coach(admin.ModelAdmin):
    list_display=('name','lastname','nation','role')

@admin.register(Player)
class Player(admin.ModelAdmin):
    list_display=('name','lastname','team','number','foto')

    def foto(self,obj):
        return format_html('<img src={} width=100 height=100 />',obj.photo.url)
    

