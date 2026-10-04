from rest_framework import serializers
from .models import Dealer,Review,CarMake,CarModel
class ReviewSerializer(serializers.ModelSerializer):
    class Meta: model=Review; fields="__all__"
class DealerSerializer(serializers.ModelSerializer):
    reviews=ReviewSerializer(many=True,read_only=True)
    class Meta: model=Dealer; fields="__all__"
class CarModelSerializer(serializers.ModelSerializer):
    class Meta: model=CarModel; fields="__all__"
class CarMakeSerializer(serializers.ModelSerializer):
    models=CarModelSerializer(many=True,read_only=True)
    class Meta: model=CarMake; fields="__all__"
