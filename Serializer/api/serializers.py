from AssetMgmt.models import Screen
from rest_framework import serializers

class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = ('id', 'deviceNumber','carRegNumber', 'carOwner' , 'carDriver' ,'carModel' ,'activeFlag', 'longitude', 'latitude','date','lastknown')

        def update(self, instance, validated_data):
       	 	instance.latitude = validated_data.get('latitude', latitude.name)
       	 	instance.save()
       	 	return instance

# class ScreenSerializerUpdate(serializers.ModelSerializer):
#     class Meta:
#         model = Screen
#         fields = ('longitude', 'latitude','id')

