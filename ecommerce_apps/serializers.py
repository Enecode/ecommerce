from decimal import Decimal
from rest_framework import serializers
from ecommerce_apps.models import Product, Collection


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'collection', 'price_with_tax']

    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    # description = serializers.HyperlinkedRelatedField()
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection = serializers.HyperlinkedRelatedField(
        required=Product.description,
        queryset=Collection.objects.all(),
        view_name='ecommerce_apps:collection_detail'
    )

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
