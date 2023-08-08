from django.db import models
from ARVappApi.models import *

#scene models
class Scene(models.Model):
    project_id=models.ForeignKey(CreateProject,on_delete=models.CASCADE)
    name=models.CharField(max_length=255,blank=True,null=True)
    FeaturedtrackerOption = models.CharField(max_length=255, blank=True)

class Scene_Transition(models.Model):
    scene_id=models.ForeignKey(Scene,on_delete=models.CASCADE)
    transition_enter=models.CharField(max_length=255,blank=True,null=True)
    transition_exit=models.CharField(max_length=255,blank=True,null=True)
    height=models.CharField(max_length=255,blank=True,null=True)
    duration=models.CharField(max_length=255,blank=True,null=True)
    delay=models.CharField(max_length=255,blank=True,null=True)

class Scene_PhotoUI(models.Model):
    scene_id=models.ForeignKey(Scene,on_delete=models.CASCADE)
    photo_ui=models.BooleanField()

#Button Tables
class Create_Button(models.Model):
    scene_id=models.ForeignKey(Scene,on_delete=models.CASCADE)
    Button_name=models.CharField(max_length=255,blank=True,null=True)

class Button_Transform(models.Model):
    button_Id=models.ForeignKey(Create_Button,on_delete=models.CASCADE,related_name='button_transform')
    width=models.CharField(max_length=255,blank=True,null=True)
    height=models.CharField(max_length=255,blank=True,null=True)
    depth=models.CharField(max_length=255,blank=True,null=True)
    position_x=models.CharField(max_length=255,blank=True,null=True)
    position_y=models.CharField(max_length=255,blank=True,null=True)
    position_d=models.CharField(max_length=255,blank=True,null=True)
    Rotation_x=models.CharField(max_length=255,blank=True,null=True)
    Rotation_y=models.CharField(max_length=255,blank=True,null=True)
    Rotation_z=models.CharField(max_length=255,blank=True,null=True)
    Mirror=models.CharField(max_length=255,blank=True,null=True)

class Button_Transition(models.Model):
    button_Id=models.ForeignKey(Create_Button,on_delete=models.CASCADE,related_name='button_transition')
    transition_enter=models.CharField(max_length=255,blank=True,null=True)
    transition_exit=models.CharField(max_length=255,blank=True,null=True)
    height=models.CharField(max_length=255,blank=True,null=True)
    duration=models.CharField(max_length=255,blank=True,null=True)
    delay=models.CharField(max_length=255,blank=True,null=True)

class Button_Text(models.Model):
    button_Id=models.ForeignKey(Create_Button,on_delete=models.CASCADE,related_name='button_text')
    text=models.CharField(max_length=255,blank=True,null=True)
    text_size=models.CharField(max_length=255,blank=True,null=True)
    text_font=models.CharField(max_length=255,blank=True,null=True)
    link=models.CharField(max_length=255,blank=True,null=True)
    text_color=models.CharField(max_length=255,blank=True,null=True)
    alignment=models.CharField(max_length=255,blank=True,null=True)

class Button_Appearance(models.Model):
    button_Id=models.ForeignKey(Create_Button,on_delete=models.CASCADE)
    corner_radius=models.CharField(max_length=255,blank=True,null=True)
    fill_Color=models.CharField(max_length=255,blank=True,null=True)
    border_width=models.CharField(max_length=255,blank=True,null=True)
    border_color=models.CharField(max_length=255,blank=True,null=True)

class Button_Action(models.Model):
    button_Id=models.ForeignKey(Create_Button,on_delete=models.CASCADE)
    button_action=models.CharField(max_length=255,blank=True,null=True)

# Text table
class Create_Text(models.Model):
    scene_id=models.ForeignKey(Scene,on_delete=models.CASCADE)
    Text_name=models.CharField(max_length=255,blank=True,null=True)

class Text_Transform(models.Model):
    text_id=models.ForeignKey(Create_Text,on_delete=models.CASCADE)
    width=models.CharField(max_length=255,blank=True,null=True)
    height=models.CharField(max_length=255,blank=True,null=True)
    depth=models.CharField(max_length=255,blank=True,null=True)
    position_x=models.CharField(max_length=255,blank=True,null=True)
    position_y=models.CharField(max_length=255,blank=True,null=True)
    position_d=models.CharField(max_length=255,blank=True,null=True)
    Rotation_x=models.CharField(max_length=255,blank=True,null=True)
    Rotation_y=models.CharField(max_length=255,blank=True,null=True)
    Rotation_z=models.CharField(max_length=255,blank=True,null=True)
    Mirror=models.CharField(max_length=255,blank=True,null=True)

class Text_Action(models.Model):
    text_id=models.ForeignKey(Create_Text,on_delete=models.CASCADE)
    text_action=models.CharField(max_length=255,blank=True,null=True)

class Text_Transition(models.Model):
    text_id=models.ForeignKey(Create_Text,on_delete=models.CASCADE)
    transition_enter=models.CharField(max_length=255,blank=True,null=True)
    transition_exit=models.CharField(max_length=255,blank=True,null=True)
    height=models.CharField(max_length=255,blank=True,null=True)
    duration=models.CharField(max_length=255,blank=True,null=True)
    delay=models.CharField(max_length=255,blank=True,null=True)

class Text_Text(models.Model):
    text_id=models.ForeignKey(Create_Text,on_delete=models.CASCADE)
    text=models.CharField(max_length=255,blank=True,null=True)
    text_size=models.CharField(max_length=255,blank=True,null=True)
    text_font=models.CharField(max_length=255,blank=True,null=True)
    link=models.CharField(max_length=255,blank=True,null=True)
    text_color=models.CharField(max_length=255,blank=True,null=True)
    alignment=models.CharField(max_length=255,blank=True,null=True)

#image tables
class ImageDesign(models.Model):
    scene_id=models.ForeignKey(Scene,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="CreateImageDesign/")

class Image_Transform(models.Model):
    image_id=models.ForeignKey(ImageDesign,on_delete=models.CASCADE)
    width=models.CharField(max_length=255,blank=True,null=True)
    height=models.CharField(max_length=255,blank=True,null=True)
    depth=models.CharField(max_length=255,blank=True,null=True)
    position_x=models.CharField(max_length=255,blank=True,null=True)
    position_y=models.CharField(max_length=255,blank=True,null=True)
    position_d=models.CharField(max_length=255,blank=True,null=True)
    Rotation_x=models.CharField(max_length=255,blank=True,null=True)
    Rotation_y=models.CharField(max_length=255,blank=True,null=True)
    Rotation_z=models.CharField(max_length=255,blank=True,null=True)
    Mirror=models.CharField(max_length=255,blank=True,null=True)

class Image_Appearance(models.Model):
    image_id=models.ForeignKey(ImageDesign,on_delete=models.CASCADE)
    frame_type=models.CharField(max_length=255,blank=True,null=True)
    opacity=models.CharField(max_length=255,blank=True,null=True)
    corner_radius=models.CharField(max_length=255,blank=True,null=True)
    border_width=models.CharField(max_length=255,blank=True,null=True)
    border_color=models.CharField(max_length=255,blank=True,null=True)

class Image_Action(models.Model):
    image_id=models.ForeignKey(ImageDesign,on_delete=models.CASCADE)
    image_action=models.CharField(max_length=255,blank=True,null=True)

class Image_Transition(models.Model):
    image_id=models.ForeignKey(ImageDesign,on_delete=models.CASCADE)
    transition_enter=models.CharField(max_length=255,blank=True,null=True)
    transition_exit=models.CharField(max_length=255,blank=True,null=True)
    height=models.CharField(max_length=255,blank=True,null=True)
    duration=models.CharField(max_length=255,blank=True,null=True)
    delay=models.CharField(max_length=255,blank=True,null=True)

#video tables
class UploadVideo(models.Model):
    scene_id=models.ForeignKey(Scene,on_delete=models.CASCADE)
    video=models.FileField(upload_to="CreateVideoDesign/")

class Video_Transform(models.Model):
    video_id=models.ForeignKey(UploadVideo,on_delete=models.CASCADE)
    width=models.CharField(max_length=255,blank=True,null=True)
    height=models.CharField(max_length=255,blank=True,null=True)
    depth=models.CharField(max_length=255,blank=True,null=True)
    position_x=models.CharField(max_length=255,blank=True,null=True)
    position_y=models.CharField(max_length=255,blank=True,null=True)
    position_d=models.CharField(max_length=255,blank=True,null=True)
    Rotation_x=models.CharField(max_length=255,blank=True,null=True)
    Rotation_y=models.CharField(max_length=255,blank=True,null=True)
    Rotation_z=models.CharField(max_length=255,blank=True,null=True)
    Mirror=models.CharField(max_length=255,blank=True,null=True)


class Video_Action(models.Model):
    video_id=models.ForeignKey(UploadVideo,on_delete=models.CASCADE)
    video_action=models.CharField(max_length=255,blank=True,null=True)

class Video_Transition(models.Model):
    video_id=models.ForeignKey(UploadVideo,on_delete=models.CASCADE)
    transition_enter=models.CharField(max_length=255,blank=True,null=True)
    transition_exit=models.CharField(max_length=255,blank=True,null=True)
    height=models.CharField(max_length=255,blank=True,null=True)
    duration=models.CharField(max_length=255,blank=True,null=True)
    delay=models.CharField(max_length=255,blank=True,null=True)

#3D Model Tables
class ThreeDModelFile(models.Model):
    scene_id=models.ForeignKey(Scene,on_delete=models.CASCADE)
    File=models.FileField(upload_to="ThreeDModelFile/")

class ThreeDModel_Transform(models.Model):
    ThreeDModel_id=models.ForeignKey(ThreeDModelFile,on_delete=models.CASCADE)
    width=models.CharField(max_length=255,blank=True,null=True)
    height=models.CharField(max_length=255,blank=True,null=True)
    depth=models.CharField(max_length=255,blank=True,null=True)
    position_x=models.CharField(max_length=255,blank=True,null=True)
    position_y=models.CharField(max_length=255,blank=True,null=True)
    position_d=models.CharField(max_length=255,blank=True,null=True)
    Rotation_x=models.CharField(max_length=255,blank=True,null=True)
    Rotation_y=models.CharField(max_length=255,blank=True,null=True)
    Rotation_z=models.CharField(max_length=255,blank=True,null=True)
    Mirror=models.CharField(max_length=255,blank=True,null=True)

class ThreeDModel_Action(models.Model):
    ThreeDModel_id=models.ForeignKey(ThreeDModelFile,on_delete=models.CASCADE)
    action=models.CharField(max_length=255,blank=True,null=True)

class ThreeDModel_Transition(models.Model):
    ThreeDModel_id=models.ForeignKey(ThreeDModelFile,on_delete=models.CASCADE)
    transition_enter=models.CharField(max_length=255,blank=True,null=True)
    transition_exit=models.CharField(max_length=255,blank=True,null=True)
    height=models.CharField(max_length=255,blank=True,null=True)
    duration=models.CharField(max_length=255,blank=True,null=True)
    delay=models.CharField(max_length=255,blank=True,null=True)



#project models
   
class Project_Content(models.Model):
     project_id=models.ForeignKey(CreateProject,on_delete=models.CASCADE)
     target_image=models.ImageField(upload_to="targetimage/" , null=True , blank=True)
     opacity=models.CharField(max_length=255,blank=True,null=True)
     orientation=models.CharField(max_length=255,blank=True,null=True)
     dimensions_w=models.CharField(max_length=255,blank=True,null=True)
     dimensions_h=models.CharField(max_length=255,blank=True,null=True)
     units=models.CharField(max_length=255,blank=True,null=True)

class Background_Sound(models.Model):
     project_content_id=models.ForeignKey(Project_Content,on_delete=models.CASCADE)
     media_file=models.FileField(upload_to="background_sound/" , null=True , blank=True)

class Analytics(models.Model):
    project_content_id=models.ForeignKey(Project_Content,on_delete=models.CASCADE)
    track_with=models.CharField(max_length=255,blank=True,null=True)

class TwoD_ThreeD_Switch(models.Model):
     scene_id=models.ForeignKey(Scene,on_delete=models.CASCADE)
     value=models.BooleanField()


# class Target_image_QR_code_image(models.Model):
#     project_id=models.ForeignKey(CreateProject,on_delete=models.CASCADE)
#     target_image_url=models.URLField()
#     user_id=models.ForeignKey(User,on_delete=models.CASCADE)
#     publish_key=models.BooleanField()
#     qr_code_url=models.URLField()
#     description=models.CharField(max_length=255,blank=True,null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

