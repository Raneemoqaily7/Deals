from rest_framework import serializers

from deal.models import User_Profile , Deal


class UserSerializer (serializers.ModelSerializer):
    class Meta :
        model = User_Profile
        fields=["id" ,"name" ,"status","email","phone","gender","Date_Of_Birth" ]




class DealSerializer(serializers.ModelSerializer):
    class Meta :
        model =Deal
        fields = ["id","name","Description","status","amount","currency"]