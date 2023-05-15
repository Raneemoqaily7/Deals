from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from deal.models import  Deal,Account



class DealSerializer(serializers.ModelSerializer):
    class Meta :
        model =Deal
        fields = ["id","name","Description","status","amount","currency" ,"DateTime_UTC","Server_DateTime","Update_DateTime_UTC"]







class ProfileSerializer (serializers.ModelSerializer):
    class Meta :
        model = Account
        fields=["id" ,"username" ,"status","email","phone","gender","Date_Of_Birth" ,"user_image","claimed_deal","is_admin","Server_DateTime","date_joined","Update_DateTime_UTC","last_login"]
        depth = 1

    # def update(self,instance,validated_data):
    #     instance.user_image=validated_data.get('user_image',instance.user_image)
    #     instance.save()
    #     return inst


 

class Registerationerializer (serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ["email", "username", "password", "password2","phone","user_image","status","gender","Date_Of_Birth"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
      
        email = self.validated_data["email"]
        username = self.validated_data["username"]
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        phone = self.validated_data["phone"]
        gender=self.validated_data["gender"]
        status=self.validated_data["status"]
        Date_Of_Birth=self.validated_data["Date_Of_Birth"]
        user_image=self.validated_data["user_image"]
        


        if password2 != password:
            raise serializers.ValidationError({'password': 'Passwords must match'})

        account = Account(email=email,user_image=user_image, username=username, password=make_password(password),Date_Of_Birth=Date_Of_Birth,phone =phone,gender=gender,status=status)
        account.save()
        return account

# class Registerationerializer (serializers.ModelSerializer):
    
#     password2=serializers.CharField(style={'input_type': 'password'},write_only=True)

#     class Meta :
#         model =Account
#         fields = ["email" ,"username" ,"password","password2"]
#         extra_kwargs = {

#             'password': {'write_only': True}
#         }

#     def save(self):
#         account =Account(
#             email =self.validated_data["email"],
            
#             username =self.validated_data["username"],
#         )        
#         password = self.validated_data["password"]
#         password2=self.validated_data["password2"]

#         if password2 !=password:
#             raise serializers.ValidationError({'password': 'Passwords must match'})
        
        
#         account.set_password(password)
#         account.save()
#         return account
















class ImageSerializer (serializers.ModelSerializer):

    class Meta :
        model = Account
        fields = ['user_image']

    def update (self,instance,validated_data):
        instance.user_image = validated_data.get('user_image' ,instance.user_image )
        instance.save()
        return  instance