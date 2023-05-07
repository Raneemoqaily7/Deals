from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

from deal import views



urlpatterns = [
    path('register/', views.registeration_view ),
    path('login/', obtain_auth_token ),



    path('user_list/', views.user_list_view),



    #get deal list 
    path('deal_list/', views.get_deal_list),




    #add new deal
    path('add_deal/', views.add_deal_view),

    

    #Update User Status
    path('update_user_status/<int:id>', views.update_user_status),

    #Update Deal 
    path('update_deal_status/<int:id>', views.update_deal_status),



    #bulk delete
    path('delete_user/', views.delete_user),


    path('upload_image/', views.upload_image),

    #get Active Deal List
    path('active-deals/', views.active_deal_list, name='active-deal-list'),
   
    
    
]
