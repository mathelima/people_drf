from django.contrib import admin
from person.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'rg')

admin.site.register(Person, PersonAdmin)

