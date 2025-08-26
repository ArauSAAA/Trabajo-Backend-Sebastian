from django.db import models

# Create your models here.
class  Person(models.Model):
    first_name =  models.CharField(max_length=50, help_text="indica tus 2 nombres")
    last_name =  models.CharField(max_length=50, help_text="indica tus 2 apellidos")
    age =  models.IntegerField(help_text="pon tu edad")
    class Meta:
        db_table = "Person"
    