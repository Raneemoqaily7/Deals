from rest_framework import serializers

from deal.models import  Deal,Account


class ProfileSerializer (serializers.ModelSerializer):
    class Meta :
        model = Account
        fields=["id" ,"username" ,"status","email","phone","gender","Date_Of_Birth" ,"user_image"]







class Registerationerializer (serializers.ModelSerializer):
    
    password2=serializers.CharField(style={'input_type': 'password'},write_only=True)

    class Meta :
        model =Account
        fields = ["email" ,"username" ,"password","password2"]
        extra_kwargs = {

            'password': {'write_only': True}
        }

    def save(self):
        account =Account(
            email =self.validated_data["email"],
            
            username =self.validated_data["username"],
        )        
        password = self.validated_data["password"]
        password2=self.validated_data["password2"]

        if password2 !=password:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        
        
        account.set_password(password)
        account.save()
        return account












class DealSerializer(serializers.ModelSerializer):
    class Meta :
        model =Deal
        fields = ["id","name","Description","status","amount","currency" ,"DateTime_UTC","Server_DateTime"]






class ImageSerializer (serializers.ModelSerializer):

    class Meta :
        model = Account
        fields = ['user_image']

    def update (self,instance,validated_data):
        instance.user_image = validated_data.get('user_image' ,instance.user_image )
        instance.save()
        return  instance