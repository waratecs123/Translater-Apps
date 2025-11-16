from django.contrib import admin
from .models import (
    Games, Staff, Vacancy, Products,
    News, Sponsors, Feedback, Cooperation
)


class GamesAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'year')
    search_fields = ('title', 'company')
    list_filter = ('year', 'company')
    readonly_fields = ('photo_preview',)

    def photo_preview(self, obj):
        if obj.photo1:
            from django.utils.html import format_html
            return format_html('<img src="{}" width="150" />', obj.photo1.url)
        return "-"

    photo_preview.short_description = 'Photo Preview'


class StaffAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'year', 'experience')
    search_fields = ('surname', 'name', 'patronymic', 'position')
    list_filter = ('position', 'year')
    readonly_fields = ('photo_preview',)

    def photo_preview(self, obj):
        if obj.photo:
            from django.utils.html import format_html
            return format_html('<img src="{}" width="150" />', obj.photo.url)
        return "-"

    photo_preview.short_description = 'Photo Preview'


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'experience_level', 'experience', 'price', 'is_actual')
    search_fields = ('title', 'experience_level')
    list_filter = ('is_actual', 'experience_level')
    readonly_fields = ('photo_preview',)

    def photo_preview(self, obj):
        if obj.photo1:
            from django.utils.html import format_html
            return format_html('<img src="{}" width="150" />', obj.photo1.url)
        return "-"

    photo_preview.short_description = 'Photo Preview'


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    search_fields = ('name', 'about')
    list_filter = ('price',)
    readonly_fields = ('photo_preview',)

    def photo_preview(self, obj):
        if obj.photo:
            from django.utils.html import format_html
            return format_html('<img src="{}" width="150" />', obj.photo.url)
        return "-"

    photo_preview.short_description = 'Photo Preview'


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'text')
    list_filter = ('created_at',)
    readonly_fields = ('photo_preview',)

    def photo_preview(self, obj):
        if obj.photo1:
            from django.utils.html import format_html
            return format_html('<img src="{}" width="150" />', obj.photo1.url)
        return "-"

    photo_preview.short_description = 'Photo Preview'


class SponsorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_name_director', 'financing')
    search_fields = ('name', 'surname_d', 'name_d', 'patronymic_d')
    list_filter = ('year',)
    readonly_fields = ('photo_preview',)

    def photo_preview(self, obj):
        if obj.photo:
            from django.utils.html import format_html
            return format_html('<img src="{}" width="150" />', obj.photo.url)
        return "-"

    photo_preview.short_description = 'Photo Preview'


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'full_name')
    search_fields = ('title', 'email', 'surname', 'name', 'patronymic')

    def full_name(self, obj):
        return f"{obj.surname} {obj.name} {obj.patronymic}"

    full_name.short_description = 'Full Name'


class CooperationAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'email', 'full_name')
    search_fields = ('title', 'company', 'email', 'surname', 'name', 'patronymic')

    def full_name(self, obj):
        return f"{obj.surname} {obj.name} {obj.patronymic}"

    full_name.short_description = 'Full Name'


admin.site.register(Games, GamesAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Sponsors, SponsorsAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Cooperation, CooperationAdmin)