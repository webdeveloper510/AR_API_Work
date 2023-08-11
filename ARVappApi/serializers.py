from rest_framework import serializers
from .models import *

# VIDEO SERIALIZER
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

# CREATE PROJECT SERIALIZER

class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateProject
        fields = '__all__'

# USER CREATION SERIALIZER

class UserRegister(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  
    def create(self, validated_data,):
       user=User.objects.create(
       email=validated_data['email'],
       firstname=validated_data['firstname'],
       lastname=validated_data['lastname'],
       dateofbirth=validated_data['dateofbirth'],
       proffession=validated_data['proffession'],
       image=validated_data['image']
       )
       user.set_password(validated_data['password'])
       user.save()
       return user

# USER LOGIN SERIALIZER

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=250)
    class Meta:
        model=User
        fields=['email','password']
        extra_kwargs={
            'email': {'error_messages': {'required': "email is required",'blank':'please provide a email'}},
            'password': {'error_messages': {'required': "password is required",'blank':'please Enter a email'}}
            
        }


# USER PROFILE SERIALIZER

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','firstname','lastname','image','dateofbirth','proffession']   


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

# PROJECT SAVE SERIALIZER

class SaveProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project3DModel
        fields = '__all__'

class CreateProject_Serializer(serializers.ModelSerializer):
     class Meta:
        model= CreateProject
        fields = '__all__'
           
     def create(self, validate_data):
         return CreateProject.objects.create(**validate_data)
     

class Project_ID_QR_Code_Serializer(serializers.ModelSerializer):
     class Meta:
        model= Project_ID_QR_Code
        fields = '__all__'
           
     def create(self, validate_data):
         return Project_ID_QR_Code.objects.create(**validate_data)
     


class ProjectLabel_Serializer(serializers.ModelSerializer):
     class Meta:
        model= ProjectLabel
        fields = '__all__'
           
     def create(self, validate_data):
         return ProjectLabel.objects.create(**validate_data)
     
class UploadFile_Serializer(serializers.ModelSerializer):
     class Meta:
        model= UploadFile
        fields = '__all__'
           
     def create(self, validate_data):
         return UploadFile.objects.create(**validate_data)
     





