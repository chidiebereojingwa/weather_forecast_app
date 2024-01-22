from django.urls import path
from . import views
from .views import index, search, detail

urlpatterns = [
    path("", index, name="index"),
    path("search/", search, name="search"),
    path("detail/<int:city_id>/", detail, name="detail"),
]
