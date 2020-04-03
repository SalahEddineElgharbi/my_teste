from django.urls import path
from myapp import views


# temlpate tagging 
app_name ='myapp'

urlpatterns= [
 
    path(r'relative/',views.relative,name = 'relative'),
    path(r'',views.index1 , name ='index1'),
    path(r'other/',views.other,name = 'other'),



]