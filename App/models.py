from django.db import models

# Create your models here.
class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"

class TurModel(models.Model):
    region=[
        ("Navoiy", "Navoiy"),
        ("Tashkent", "Tashkent")
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    region = models.CharField(max_length=300, choices=region)
    images = models.TextField()
    images = models.JSONField()  
    location = models.OneToOneField(Location, on_delete=models.CASCADE)



