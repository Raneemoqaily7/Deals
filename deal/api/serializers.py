from rest_framework import serializers

from deal.models import User_Profile , Deal


class UserSerializer (serializers.ModelSerializer):
    class Meta :
        model = User_Profile
        fields=["id" ,"name" ,"status","email","phone","gender","Date_Of_Birth" ,"user_image"]




class DealSerializer(serializers.ModelSerializer):
    class Meta :
        model =Deal
        fields = ["id","name","Description","status","amount","currency"]


class ImageSerializer (serializers.ModelSerializer):

    class Meta :
        model = User_Profile
        fields = ['user_image']

    def update (self,instance,validated_data):
        instance.user_image = validated_data.get('user_image' ,instance.user_image )
        instance.save()
        return  instance