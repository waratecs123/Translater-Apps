from django.contrib import admin
from .models import Race, Class, Skill, Spell, Character, Attribute, Type, Item, InventoryItem

# Register your models here.
class RaceAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ['name']
    search_fields = ['name']


class ClassAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ['name']
    search_fields = ['name']


class SkillAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ['name']
    search_fields = ['name']


class SpellAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ['name']
    search_fields = ['name']


class CharacterAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ['name']
    search_fields = ['name']


class AttributeAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ['character']
    search_fields = ['character']


class TypeAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ['name']
    search_fields = ['name']


class ItemAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ['name']
    search_fields = ['name']


class InventoryItemAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ['character']
    search_fields = ['character']


admin.site.register(Race, RaceAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Spell, SpellAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(InventoryItem, InventoryItemAdmin)