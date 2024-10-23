from django.urls import path
from .views import serve_image,login,index,logout

urlpatterns =[
    path('login/',login,name='login'),
    path('image/',serve_image, name='image-serve'),
    path('logout/',logout, name='logout'),
    path('',index, name='index'),
]