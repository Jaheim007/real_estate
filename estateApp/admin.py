from django.contrib import admin
from . models import Info

class InfoShow(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'password', 'confirmPassword')
admin.site.register(Info, InfoShow)

# Register your models here.
