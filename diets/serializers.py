from rest_framework import serializers

from .models import ImageAlbum, ImageCDN, Nutrition, Food, Category, Custom


class ImageAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageAlbum
        fields = "__all__"


class ImageCDNSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCDN
        fields = "__all__"


class NutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrition
        fields = "__all__"


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom
        fields = "__all__"
