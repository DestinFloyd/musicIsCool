from django.db import models

# Create your models here.

class Test(models.Model):
    testId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
