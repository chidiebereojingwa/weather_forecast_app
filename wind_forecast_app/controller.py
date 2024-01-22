import requests
from .models import WeatherForecast

API_KEY = "b793b5b54a0dcc7bdcae97ad438525a6"


class WeatherController:
    @staticmethod
    def get_city_locations(city_name):
        api_url = (
            f"http://api.openweathermap.org/data/2.5/find?q={city_name}&appid={API_KEY}"
        )
        response = requests.get(api_url)
        data = response.json()

        locations = []
        for city in data.get("list", []):
            locations.append(
                {
                    "id": city["id"],
                    "name": city["name"],
                    "country": city["sys"]["country"],
                }
            )

        return locations

    @staticmethod
    def get_forecast(city_id):
        api_url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}"
        response = requests.get(api_url)
        forecast_data = response.json()

        weather_forecast, _ = WeatherForecast.objects.get_or_create(
            city_name=forecast_data["name"],
            country=forecast_data["sys"]["country"],
            defaults={
                "temperature": forecast_data["main"]["temp"],
                "description": forecast_data["weather"][0]["description"],
                "wind_speed": forecast_data["wind"]["speed"],
                "wind_direction": forecast_data["wind"]["deg"],
                "humidity": forecast_data["main"]["humidity"],
                "icon": forecast_data["weather"][0]["icon"],
            },
        )

        return {
            "city_name": weather_forecast.city_name,
            "country": weather_forecast.country,
            "temperature": weather_forecast.temperature,
            "description": weather_forecast.description,
            "wind_speed": weather_forecast.wind_speed,
            "wind_direction": weather_forecast.wind_direction,
            "humidity": weather_forecast.humidity,
            "icon": weather_forecast.icon,
        }
