from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser ,FormParser

from deal.models import User_Profile ,Deal
from deal.api.serializers import UserSerializer ,DealSerializer ,ImageSerializer 

# Create your views here.

@api_view (['GET','POST'])

def user_list_view (request):
    if request.method == 'GET':
        user = User_Profile.objects.all()
        serializer = UserSerializer(user ,many=True)
        
        return Response (serializer.data)
    
    elif request.method == 'POST':
        serializer =UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()

            return Response (serializer.data , status=status.HTTP_201_CREATED)
        return Response (serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    



@api_view (["GET","POST"])

def deal_list_view (request):

    if request.method =="GET":

        deal = Deal.objects.all()
        serializer = DealSerializer(deal , many=True)
        return Response(serializer.data)
    

    if request.method == "POST":
        serializer = DealSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data ,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors ,status =status.HTTP_400_BAD_REQUEST)



@api_view (["PATCH"])
def update_user_status(request,id):
    try :
     user =User_Profile.objects.get(id=id)

    except User_Profile.DoesNotExist:
        return Response(status =status.HTTP_404_NOT_FOUND)
    
    if request.method == "PATCH":
        serializer=UserSerializer(user , request.data , partial= True )
        data= {}
        if serializer.is_valid():
            serializer.save()
            data["success"]="status updated successfully"
            return Response(data= data)
        
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)



@api_view (["DELETE"])

#id__in filter to filter the users you want to delete and then call the delete()


def delete_user (request):
   
    try:
        users_id = request.data.get('users_id', [])

    except User_Profile.DoesNotExist :
        return Response (status =status.HTTP_404_NOT_FOUND)
    data ={}
    if not users_id :
        return Response({'error': 'user id is  required'}, 
                        status=status.HTTP_400_BAD_REQUEST)
    
    users = User_Profile.objects.filter(id__in=users_id)
    users.delete()
    data["success"]="delete successful"
    return Response(data=data, status=status.HTTP_204_NO_CONTENT)

        



            




    
@api_view (["POST"])
@parser_classes([MultiPartParser ,FormParser])
def upload_image(request,format =None):
    if request.method == "POST":
        user =request.user
        serializer=ImageSerializer(instance =user ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data =serializer.data ,status=status.HTTP_201_CREATED)


        else :

          return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)