from django.contrib import admin

from .models import ImageAlbum, ImageCDN, Nutrition, Food, Category, Custom


# Register your models here.
admin.site.register(ImageAlbum)
admin.site.register(ImageCDN)
admin.site.register(Nutrition)
admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Custom)
