from django.db import models

# Create your models here.
class TodoModel(models.Model):
    
    STATUS =(
        ('Complete','Complete'),
        ('In-Complete','In-Complete'),    
    )
    id = models.IntegerField(primary_key = True)
    Title = models.CharField(max_length=100)
    Description = models.CharField( max_length=250)
    Status = models.CharField( max_length=50 ,choices =STATUS)
    