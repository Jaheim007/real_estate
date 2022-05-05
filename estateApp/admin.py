from django.contrib import admin
from . models import Sign

class InfoShow(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'username', 'password', 'confirm_Password')
admin.site.register(Sign, InfoShow)

# Register your models here.
