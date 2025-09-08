from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=50, help_text="ingresa tu nombre")
    last_name = models.CharField(max_length=50, help_text="ingresa tu apellido")
    age = models.IntegerField(help_text="ingresa tu edad")
    
    class Meta:
        db_table = "Persona"
        #modificar el nombre
        # verbose_name = "Persona"
        # verbose_name_prural = "Personas"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Estudiantes(models.Model):
    first_name = models.CharField(max_length=50, help_text="ingresa tu nombre")
    last_name = models.CharField(max_length=50, help_text="ingresa tu apellido")
    age = models.IntegerField(help_text="ingresa tu edad")
    enrollment_date = models.DateField(help_text="ingresa la fecha de inscripción")
    
    class Meta:
        db_table = "Estudiantes"
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"    