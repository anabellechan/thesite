from rest_framework import serializers 
from customers.models import Customers
 
 
class CustomerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Customers
        fields = (
                  'customerid',
                  'firstname',
                  'lastname',
                  'company',
                  'city',
                  'country',
                  'phone1',
                  'phone2',
                  'email',
                  'subscriptiondate',
                  'website',
                  'filename_index')
        
        
class CustomerBulkCreateSerializer(serializers.ListSerializer):  
        def create(self, validated_data):  
            product_data = []
            batch_size = 1000
            for i in range(0, len(validated_data), batch_size):
                batch = validated_data[i:i+batch_size]
                product_data += [Customers(**item) for item in batch] 
            return Customers.objects.bulk_create(product_data)  
      

class CustomersBulkSerializer(serializers.ModelSerializer):  
        class Meta:  
            model = Customers
            fields = ['customerid',
                  'firstname',
                  'lastname',
                  'company',
                  'city',
                  'country',
                  'phone1',
                  'phone2',
                  'email',
                  'subscriptiondate',
                  'website',
                'filename_index']  
            # read_only_fields = ['index']  
            list_serializer_class = CustomerBulkCreateSerializer  