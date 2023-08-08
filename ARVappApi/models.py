from django.db import models
from django.contrib.auth.models import *
from django.contrib.auth.models import UserManager


# class User(AbstractUser):
class User(AbstractBaseUser, PermissionsMixin):
    CHOICES = [
        ('I am a Designer.','I am a Designer.'),
        ('I am a Developer.','I am a Developer.'),
        ('I am a Marketer.','I am a Marketer.'),
        ('I am a Educator.','I am a Educator.'),
        ('I am a 3D Artist.','I am a 3D Artist.'),
        ('I am working in Learning and Development.','I am working in Learning and Development.'),
        ('Something Else.','Something Else.'),
    ]

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=255,unique=True,)
    password = models.CharField(max_length=100)
    image=models.ImageField(upload_to='profile_picture/',blank=True,null=True)
    dateofbirth = models.DateField()
    proffession = models.TextField(choices=CHOICES, max_length=200)
    Is_verified=models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
   
      

class Video(models.Model):
    video = models.FileField(upload_to='videos/')
    userId = models.ForeignKey(User ,  on_delete=models.CASCADE)

    def __unicode__(self):
                return (self.video)
    def image_img(self):
        if self.video:
            return u'<video src="%s" width="50" height="50" />' % self.video.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True


import uuid
def new_uuid() -> uuid.UUID:
   
        val = uuid.uuid4()
        while val.hex[0] == '0':
            val = uuid.uuid4()
        return val

class CreateProject(models.Model):
    id = models.UUIDField(primary_key=True, default=new_uuid,editable=False)
    projectType = models.CharField(max_length=50)
    triggerType = models.CharField(max_length=50)
    imagePro = models.FileField(upload_to='image', blank=True,null=True)
    ProTitle = models.CharField(max_length=255,default="Untitled",null=True)
    projectIcon = models.FileField(upload_to='image',blank=True,null=True)
    projectTitle = models.CharField(max_length=255 ,blank=True,null=True)
    projectUser = models.ForeignKey(User,blank=False , on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    publish_key=models.BooleanField(default=False)
    

    # def __str__(self):
    #     return self.created_at.strftime('%Y-%m-%d')

    def __unicode__(self):
                return (self.imagePro)
    def image_img(self):
        if self.imagePro:
            return u'<img src="%s" width="50" height="50" />' % self.imagePro.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True     


class Project_ID_QR_Code(models.Model):
    project_id=models.ForeignKey(CreateProject,on_delete=models.CASCADE)
    project_id_qr_code_url=models.URLField()
    qr_code_url=models.URLField()
    publish_key=models.BooleanField(default=False)
    description=models.CharField (blank=True,null=True,max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Project3DModel(models.Model):
    model3D = models.FileField(upload_to='3Dmodel')
    videoId = models.ForeignKey(Video, null=True, blank=True, on_delete=models.CASCADE)
    projectId = models.ForeignKey(CreateProject, null=True, blank=True, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
     
class ProjectLabel(models.Model):
    projectId = models.ForeignKey(CreateProject, null=True, blank=True, on_delete=models.CASCADE)
    project_label=models.CharField (blank=True,null=True,max_length=250)
    user_id=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    required=models.BooleanField()

class UploadFile(models.Model):
    user_id=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    file=models.FileField(upload_to="File/")
     