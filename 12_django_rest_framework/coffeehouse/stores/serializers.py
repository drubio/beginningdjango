from rest_framework import serializers

from coffeehouse.stores.models import Store

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
        
