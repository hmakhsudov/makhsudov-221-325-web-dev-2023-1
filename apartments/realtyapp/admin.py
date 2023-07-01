from django.contrib import admin
from .models import ApartmentImage, Apartment, Favorites, Purchases




class ApartmentImageInline(admin.TabularInline):
    model = ApartmentImage
    extra = 3

class ApartmentAdmin(admin.ModelAdmin):
    inlines = [ApartmentImageInline, ]


admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Favorites)
admin.site.register(Purchases)
