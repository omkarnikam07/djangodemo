from django.db import models

# Create your models here.

class AddStudent2(models.Model):
    # ...
    def __str__(self):
        return self.name
