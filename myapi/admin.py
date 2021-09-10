from django.contrib import admin
from .models import changed,broke,Product, color, mod,Image
# Register your models here.
# admin.register() decorator

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'year', 'color','mod',)

   
admin.site.register(changed)
admin.site.register(broke)
admin.site.register(mod)
admin.site.register(color)
admin.site.register(Image)
