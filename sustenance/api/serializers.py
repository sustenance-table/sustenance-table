from rest_framework import serializers

from api.models import Book, Category, Nutrient, Benefit, Origin, Item


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = ('id', 'name')


class NutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrient
        fields = ('id', 'name')


class OriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origin
        fields = ('id', 'name')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'item_categories', '')