from django.db import models

class WeatherForecast(models.Model):
    city_name = models.CharField(max_length=255)
    country = models.CharField(max_length=2)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    wind_speed = models.FloatField()
    wind_direction = models.FloatField()
    humidity = models.FloatField()
    icon = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.city_name}, {self.country}"
