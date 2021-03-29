from django.urls import path

from . import views

urlpatterns = [
    path("nutrition", views.NutritionView.as_view()),
    path("food", views.FoodView.as_view()),
    path("category", views.CategoryView.as_view()),
    path("custom", views.CustomView.as_view()),
    path("album", views.AlbumView.as_view()),
    path("image", views.ImageCDNView.as_view()),
]
