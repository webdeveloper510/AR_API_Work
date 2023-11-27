#ARVappApi packages

from rest_framework import generics , status , viewsets
# from .models import Video
from rest_framework.views import APIView 
from rest_framework.response import Response
# from .serializers import *
from distutils import errors
from django.conf import settings
from django.contrib.auth import logout,login,authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from rest_framework import status, views
from rest_framework_simplejwt.tokens import RefreshToken
import  json
from django.http import JsonResponse
from django.conf import settings
from django.http import Http404
from ARVappApi.renderer import UserRenderer
# url="http://127.0.0.1:8000"
url="http://13.232.225.65:8000"
from urllib.parse import urljoin
from django.core.exceptions import ValidationError
import os
import qrcode 
import sys
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMultiAlternatives, message
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
import numpy as np
# image_url="http://127.0.0.1:8000/media/"
image_url="http://13.232.225.65:8000/media/"

# Project_Id_Url="http://127.0.0.1:3000/#/ar-web-view"
Project_Id_Url="http://13.232.225.65/#/ar-web-view"
# Verify_url="http://127.0.0.1:3000/#/verify-email"
Verify_url="http://13.232.225.65/#/verify-email"
# Forget_password_url="http://127.0.0.1:3000/#/forgot-password"
Forget_password_url="http://13.232.225.65/#/forgot-password"


from ARVappApi.serializers import *
from ARVappApi.models import *


#product app Packages 

from django.shortcuts import render
from productapp.models import *
from ARVappApi.models import *
from rest_framework import viewsets
from productapp.serializers import *
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework import status, views
from rest_framework import generics
from django.shortcuts import get_object_or_404
# url="http://127.0.0.1:8000"
url="http://13.232.225.65:8000"
from urllib.parse import urljoin
from django.http import Http404
# background_url="http://127.0.0.1:8000/media/"
background_url="http://13.232.225.65:8000/media/"
# Create button Api 
from productapp.utilities import URLEncrypter
import qrcode 
import sys
from productapp.serializers import *
from productapp.models import *