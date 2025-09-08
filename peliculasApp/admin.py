from django.contrib import admin
from .models import Person, Estudiantes

class PersonAdmin(admin.ModelAdmin):
    list_display = ("id","first_name", "last_name", "age")
    list_filter = ("last_name",)

class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ("id","first_name", "last_name", "age", "enrollment_date")
    list_filter = ("last_name",)

# Register your models here.
admin.site.register(Person, PersonAdmin)                                  
admin.site.register(Estudiantes, EstudiantesAdmin)                                