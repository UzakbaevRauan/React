from django.urls import path
from .views import register_user,login_user

app_name = 'Rauan'
urlpatterns = [
   path('register/', register_user, name='register'),
   path('login/', login_user, name='login'),
   

]