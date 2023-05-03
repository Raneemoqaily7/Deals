from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from deal.models import User_Profile ,Deal
from deal.api.serializers import UserSerializer ,DealSerializer

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

    

    


