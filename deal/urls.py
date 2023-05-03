from django.urls import path,include

from deal import views



urlpatterns = [
    path('user_list/', views.user_list_view),
    path('deal_list/', views.deal_list_view),
    
]
