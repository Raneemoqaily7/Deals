from django.urls import path,include

from deal import views



urlpatterns = [
    path('user_list/', views.user_list_view),
    path('deal_list/', views.deal_list_view),
    path('update_status/<int:id>', views.update_user_status),
    path('delete_user/', views.delete_user),
    path('upload_image/', views.upload_image),
    
]
