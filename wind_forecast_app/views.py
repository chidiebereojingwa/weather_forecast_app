from django.shortcuts import render, redirect
from .controller import WeatherController

def index(request):
    return render(request, "index.html")

def search(request):
    if request.method == "POST":
        city_name = request.POST["city"]
        locations = WeatherController.get_city_locations(city_name)
        return render(
            request, "index.html", {"locations": locations, "selected_city": city_name}
        )
    return redirect(
        "index"
    )  


def detail(request, city_id):
    forecast = WeatherController.get_forecast(city_id)
    return render(request, "detail.html", {"forecast": forecast})
