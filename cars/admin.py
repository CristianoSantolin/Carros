from django.contrib import admin
from cars.models import car, Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class carAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(car, carAdmin)

