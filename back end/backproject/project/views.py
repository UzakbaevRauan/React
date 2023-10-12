from django.shortcuts import render
from django.http import JsonResponse
from .models import UserProfile
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register_user(request):
  
  response = HttpResponse()
  response["Access-Control-Allow-Origin"] = "http://localhost:3000"
    
  if request.method == 'POST':
        
      data = json.loads(request.body) 
      first_name = data.get('first_name')
      last_name = data.get('last_name')
      email = data.get('email')
      password = data.get('password')
      avatarUrl = data.get('AvatarUrl')
      usertag = data.get('usertag')
      department = data.get('department')
      birthday = data.get('birthday')
      phone= data.get('phone')
      # Create a new user profile
      user_profile = UserProfile(first_name=first_name, last_name=last_name, 
                                 email=email, password=password,avatarUrl=avatarUrl,
                                 usertag=usertag,department=department,birthday=birthday,phone=phone)
      user_profile.save()
      
      return JsonResponse({'message': 'User registered successfully'})
    
  return JsonResponse({'message': 'Invalid request method'})



@csrf_exempt
def login_user(request):
    response = JsonResponse({})  # Provide initial empty data
    response["Access-Control-Allow-Origin"] = "http://localhost:3000"

    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            email = data.get('email')
            password = data.get('password')
            user_exists = UserProfile.objects.filter(email=email, password=password).exists()

            return JsonResponse({'user_exists': user_exists})
        except json.JSONDecodeError as e:
            response.status_code = 400  # Bad Request
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        response.status_code = 405  # Method Not Allowed
        return response
