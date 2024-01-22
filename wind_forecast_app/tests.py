from django.test import TestCase, Client
from .models import WeatherForecast
from .controller import WeatherController


class WeatherControllerTest(TestCase):
    def setUp(self):
       
        self.city_name = "TestCity"
        self.city_id = 12345

    def test_get_city_locations(self):
    
        locations = WeatherController.get_city_locations(self.city_name)

        self.assertTrue(isinstance(locations, list))
        self.assertTrue(all(isinstance(location, dict) for location in locations))
        self.assertTrue(
            all(
                "id" in location and "name" in location and "country" in location
                for location in locations
            )
        )

    def test_get_forecast(self):

        forecast = WeatherController.get_forecast(self.city_id)

        self.assertTrue(isinstance(forecast, dict))
        self.assertTrue(
            all(
                key in forecast
                for key in [
                    "city_name",
                    "country",
                    "temperature",
                    "description",
                    "wind_speed",
                    "wind_direction",
                    "humidity",
                    "icon",
                ]
            )
        )

        weather_forecast = WeatherForecast.objects.filter(
            city_name=forecast["city_name"], country=forecast["country"]
        ).first()
        self.assertIsNotNone(weather_forecast)

        # Check if the values match between the forecast and the database entry
        self.assertEqual(forecast["temperature"], weather_forecast.temperature)
        self.assertEqual(forecast["description"], weather_forecast.description)
        self.assertEqual(forecast["wind_speed"], weather_forecast.wind_speed)
        self.assertEqual(forecast["wind_direction"], weather_forecast.wind_direction)
        self.assertEqual(forecast["humidity"], weather_forecast.humidity)
        self.assertEqual(forecast["icon"], weather_forecast.icon)

    def test_detail_view(self):
        client = Client()
        response = client.get(f"/detail/{self.city_id}/")

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Temperature:")
        self.assertContains(response, "Wind Speed:")
        
