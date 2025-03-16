from rest_framework import serializers
from watchlist_app.models import Shoes, Category, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        exclude = ['id']
       
class ReviewSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Review
        exclude = ('shoes',)
        
class ShoeSerializer(serializers.ModelSerializer):
    
    precio_con_iva = serializers.SerializerMethodField()
    category = CategorySerializer()
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Shoes
        exclude =['price']
        read_only_fields = [ 'name']
        extra_kwargs = {
            'description': {'write_only': True},
            'price':{'min_value': 100}
        }
        
    def get_precio_con_iva(self, obj):
        return obj.price * 1.19

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short')
        return value

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError(
                'Name and Description should be different')
        return data
    

