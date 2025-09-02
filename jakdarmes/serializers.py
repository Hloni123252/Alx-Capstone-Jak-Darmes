cat > store/serializers.py << 'PY'
from rest_framework import serializers
from .models import Product, Category, Customer, Order, OrderItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # category rendered as nested read-only (clean for lists)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'  

    def get_items(self, obj):
        qs = OrderItem.objects.filter(order=obj)
        return OrderItemSerializer(qs, many=True).data
PY
