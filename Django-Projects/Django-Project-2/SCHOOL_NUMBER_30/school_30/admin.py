from django.contrib import admin
from .models import News, Vacancy, Staff, SchoolDocument, Sponsors

class NewsAdmin(admin.ModelAdmin):
    list_display = ('heading', 'main_category', 'audience_category', 'thematic_category')

class VacancyAdmin(admin.ModelAdmin):
    list_display = ('heading', 'is_actual')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'phone')

class SchoolDocumentAdmin(admin.ModelAdmin):
    list_display = ('heading', 'text')

class SponsorsAdmin(admin.ModelAdmin):
    list_display = ('heading', 'about')

admin.site.register(News, NewsAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(SchoolDocument, SchoolDocumentAdmin)
admin.site.register(Sponsors, SponsorsAdmin)