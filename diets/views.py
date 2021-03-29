from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db import IntegrityError
from django.http.request import QueryDict

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .imagekit import get_image_url, upload_image, delete_image
from .models import ImageAlbum, ImageCDN, Nutrition, Food, Category, Custom
from .serializers import ImageAlbumSerializer, ImageCDNSerializer, NutritionSerializer, FoodSerializer, CategorySerializer, CustomSerializer

import base64


# Create your views here.
class NutritionView(GenericAPIView):
    serializer_class = NutritionSerializer

    def get(self, request, *args, **kwargs):
        try:
            nutrition = Nutrition.objects.get(id=request.data["id"])
            return Response(NutritionSerializer(nutrition, many=True).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):

        nutrition_obj = Nutrition.objects.create(
            name=request.data["name"],
            ingredients=request.data["ingredients"],
        )
        return Response(NutritionSerializer(nutrition_obj).data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        try:
            nutrition = get_object_or_404(Nutrition, id=request.data["id"])
            nutrition.name = request.data["name"]
            nutrition.save()

            return Response(NutritionSerializer(nutrition).data, status=status.HTTP_200_OK)

        except IntegrityError:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        try:
            nutrition = get_object_or_404(Nutrition, id=request.data["id"])
            nutrition.ingredients[f"{request.data['new_key']}"] = request.data['new_value']

            if len(request.data) > 3:
                del nutrition.ingredients[f"{request.data['old_key']}"]

            nutrition.save()

            return Response(NutritionSerializer(nutrition).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            nutrition = get_object_or_404(Nutrition, id=request.data["id"])
            nutrition.delete()

            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class FoodView(GenericAPIView):
    serializer_class = FoodSerializer

    def get(self, request, *args, **kwargs):
        try:
            food = Food.objects.get(id=request.data["id"])
            return Response(FoodSerializer(food).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CategoryView(GenericAPIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        try:
            category = Category.objects.get(id=request.data["id"])
            return Response(CategorySerializer(category).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CustomView(GenericAPIView):
    serializer_class = CustomSerializer

    def get(self, request, *args, **kwargs):
        try:
            custom = Custom.objects.get(id=request.data["id"])
            return Response(CustomSerializer(custom).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AlbumView(GenericAPIView):
    serializer_class = ImageAlbumSerializer

    def get(self, request, *args, **kwargs):
        try:
            album = ImageAlbum.objects.get(id=request.data["id"])
            return Response(ImageAlbumSerializer(album).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        try:
            album_obj = ImageAlbum.objects.create(name=request.data["name"])
            return Response(ImageAlbumSerializer(album_obj).data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            album = ImageAlbum.objects.get(id=request.data["id"])
            album.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ImageCDNView(GenericAPIView):
    serializer_class = ImageCDNSerializer

    def get(self, request, *args, **kwargs):
        try:
            images = ImageCDN.objects.filter(album_id=request.data["id"])
            return Response(ImageCDNSerializer(images, many=True).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        try:
            images = request.FILES
            query_images = QueryDict("", mutable=True)
            query_images.update(images)
            images_list = query_images.getlist("photo")

            for photo in images_list:
                imgstr = base64.b64encode(photo.file.read())

                album = ImageAlbum.objects.get(id=request.data["album_id"])
                image = upload_image(imgstr, str(photo))
                imageCDN_obj = ImageCDN.objects.create(
                    album=album,
                    file_id=image["fileId"],
                    name=image["name"],
                    url=image["url"],
                    thumbnail=image["thumbnailUrl"],
                    file_type=image["fileType"]
                )

            images_CDN = ImageCDN.objects.all().order_by(
                "id").reverse()[:len(images_list)]
            return Response(ImageCDNSerializer(reversed(images_CDN), many=True).data, status=status.HTTP_201_CREATED)
        except:
            return Response(ImageCDNSerializer(status=status.HTTP_400_BAD_REQUEST))

    def delete(self, request, *args, **kwargs):
        try:
            image = ImageCDN.objects.get(id=request.data["id"])
            success = delete_image(image.file_id)
            if success:
                image.delete()
                return Response(status=status.HTTP_200_OK)
            return Response({"ERROR": "Please cross check the CDN & the Database."}, status=status.HTTP_403_FORBIDDEN)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
