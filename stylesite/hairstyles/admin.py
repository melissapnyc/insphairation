from django.contrib import admin
from hairstyles.models import Style, Image

class ImageInline(admin.StackedInline):
    model = Image
    extra = 0
    
class HairstyleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Length', {'fields': ['length']}),
        ('Texture', {'fields': ['texture']}),
        ('Time of Day', {'fields': ['time_of_day']}),
        ('Type', {'fields': ['type']}),
    ]
    inlines = [ImageInline]
    
admin.site.register(Style, HairstyleAdmin)