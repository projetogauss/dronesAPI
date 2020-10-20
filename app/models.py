from django.db import models

# Create your models here.

class DroneCategory(models.Model):
    name = models.CharField(max_length=250)

    #order by name
    class Meta:
        ordering = ("name",)
    
    class __str__(self):
        return self.name
    
class Drone(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    dronecategory = models.ForeignKey('DroneCategory',
                                       related_name='drones',
                                       on_delete=models.CASCADE)
    manufacturing_date = models.DateTimeField()
    has_it_competed = models.BooleanField(defaul=False)
    inserted_timestamp = models.DateTime(auto_now_add=True)

    class Meta:
        ordering = ("name",)

    class __str__(self):
        return self.name

class Pilot(models.Model):
    MALE = 'M'
    FAMELE = 'F'
    GENDER_CHOICES = (
        (MALE,'Male'),
        (FAMELE,'Famale'),
    )
