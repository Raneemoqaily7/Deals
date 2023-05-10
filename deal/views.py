from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes,permission_classes 
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.parsers import MultiPartParser ,FormParser

from deal.models import Deal,Account
from deal.api.serializers import DealSerializer ,ImageSerializer ,ProfileSerializer,Registerationerializer

from rest_framework.authtoken.models import Token


# Create your views here.

#registeration view 
@api_view(["POST"])
def registeration_view (request):
    if request.method =="POST":
        serializer = Registerationerializer(data =request.data)
        data={}
        if serializer.is_valid():
            account = serializer.save()
            data["response"] = "successfully registerd"
            data["email"] = account.email
            data["username"] = account.username
            token =Token.objects.get(user=account).key
            data["token"] =token
        else :
            data=serializer.errors
        return Response (data)




@api_view (['GET'])

def user_deatail_view (request ,id):
    if request.method == 'GET':
        try:

          user = Account.objects.get(id=id)
        except Account.DoesNotExist:
            return Response (status =status.HTTP_404_NOT_FOUND )
        serializer = ProfileSerializer(user )
        
        return Response (serializer.data)







@api_view (['GET','POST'])

def user_list_view (request):
    if request.method == 'GET':
        user = Account.objects.all()
        serializer = ProfileSerializer(user ,many=True)
        
        return Response (serializer.data)
    

#add user wiith claimed deal
@api_view (['POST'])

def add_user (request):  
    print (request.data ,"rrrrrrrrrrrrrrrrrrr")
    if request.method == 'POST':
        serializer =ProfileSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()

            return Response (serializer.data , status=status.HTTP_201_CREATED)
        return Response (serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    


# api_view(["POST"])
# def add_deal (request):
#     if request.method =="POST":
#         serializer = ProfileSerializer(data =request.data)
#         if serializer.is_valid ():
#             serializer.save()
#             return Response (serializer.data)




#get deal list
@api_view(['GET'])
def get_deal_list(request):
    try:
        deal = Deal.objects.all()
    except Deal.DoesNotExist:
        return Response(status =status.HTTP_404_NOT_FOUND)
    if request.method =="GET":
        serializer = DealSerializer(deal ,many=True)
        return Response(serializer.data)









## add new deal

@api_view (["POST"])

def add_deal_view(request):

    if request.method == "POST":
        serializer = DealSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data ,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors ,status =status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
def active_deal_list(request):
    queryset = Deal.objects.filter(status=Deal.Active)
    serializer = DealSerializer(queryset, many=True)
    return Response(serializer.data)











@api_view (["PATCH"])
def update_user_status(request,id):
    try :
     user =Account.objects.get(id=id)

    except Account.DoesNotExist:
        return Response(status =status.HTTP_404_NOT_FOUND)
    
    if request.method == "PATCH":
        serializer=ProfileSerializer(user , request.data , partial= True )
        data= {}
        if serializer.is_valid():
            serializer.save()
            data["success"]="User status updated successfully"
            return Response(data= data)
        
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)








@api_view (["PATCH"])
def update_deal_status(request,id):
    try :
        deal =Deal.objects.get(id=id)
    except Deal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =="PATCH":
        serializer = DealSerializer(deal ,request.data,partial=True)
        data ={}
        if serializer.is_valid():
            serializer.save()
            data["success"]="Deal status updated successfully"
            return Response(data =data)
        
        return Response(serializer.errors , status.HTTP_400_BAD_REQUEST)





@api_view (["DELETE"])

# @permission_classes([IsAdminUser])

#id__in filter to filter the users you want to delete and then call the delete() in req.bdy {'users_id': [1,2,3]}


def delete_user (request):
    print(request.data ,"rrrrrrrrrrrrrrrrrr")
    try:
        users_id = request.data.get('users_id', [])
        print(users_id ,"usersssssssss id")

    except Account.DoesNotExist :
        return Response (status =status.HTTP_404_NOT_FOUND)
    data ={}
    if not users_id :
        return Response({'error': 'user id is  required'}, 
                        status=status.HTTP_400_BAD_REQUEST)
    
    users = Account.objects.filter(id__in=users_id)
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




@api_view(["GET"])
def get_claimed_deal (request):
    user =request.user






# @api_view(['GET', 'PUT'])
# def profile_api_view(request):
#     try:
#         profile = request.user.profile
#     except User_Profile.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ProfileSerializer(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)



#Authentication =>Header -->Authorization -->Token "token"