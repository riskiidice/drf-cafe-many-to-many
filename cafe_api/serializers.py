from rest_framework import serializers

from .models import Order, Meal

class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Meal
        fields = ('name','price')

class OrderListSerializer(serializers.ModelSerializer):

    meals = MealSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'table_number', 'meals','total_price')


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id','table_number','meals')

    def create(self, validated_data):
        meals = validated_data.pop('meals')
        instance = Order.objects.create(**validated_data)

        for meal in meals:
            instance.meals.add(meal)

        return instance
