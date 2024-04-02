from django.db import models

class Place(models.Model):
    image = models.ImageField(upload_to='Media/images/places/')
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class HeritageSite(models.Model):
    image = models.ImageField(upload_to='images/HeritageSites/')
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class State_details(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_image = models.ImageField(upload_to='images/States/')
    state_name = models.CharField(max_length=255)
    state_description = models.TextField()
    state_video = models.FileField(upload_to='Media/State/', null=True, blank=True)


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    state_id = models.ForeignKey(State_details, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=255)
    city_description = models.TextField()
    city_videos =models.FileField(upload_to='Media/City/', null=True, blank=True)
    city_image = models.ImageField(upload_to='images/Cities/')


class Gallery(models.Model):
    gallery_id=models.AutoField(primary_key=True)
    state_id = models.ForeignKey(State_details, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/Gallery/')

class Location(models.Model):
    location_id=models.AutoField(primary_key=True)
    city_id=models.ForeignKey(City,on_delete=models.CASCADE)
    location_image=models.ImageField(upload_to='images/location/')
    location_videos = models.FileField(upload_to='Media/Location/', null=True, blank=True)
    location_description=models.TextField()
    location_name=models.CharField(max_length=255)


