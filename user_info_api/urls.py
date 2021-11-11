from django.urls import path
from user_info_api import views

urlpatterns = [
    path('getuserlist/', views.user_info_list, name='getuserlist'),
    path('getuserlist/name=<str:name>', views.user_info_list, name='getuser_name'),
    path('getuserlist/phone=<str:phone>', views.user_info_list, name='getuser_phone'),
    path('insertuser/', views.insert_user_info, name='insertuser'),
    path('updateuser/id=<int:id>', views.user_info_detail, name='updateuser'),
    path('deleteuser/id=<int:id>', views.user_info_detail, name='deleteuser'),
]
