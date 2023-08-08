from rest_framework import serializers
from productapp.models import *


#Button Serializers
class ButtonSerializer(serializers.ModelSerializer):
     class Meta:
        model= Create_Button
        fields = '__all__' 
     def create(self, validate_data):
         return Create_Button.objects.create(**validate_data)
     
     
class ButtonTransformSerializer(serializers.ModelSerializer):
    class Meta:
        model= Button_Transform
        fields = '__all__' 
    def create(self, validate_data):
         return Button_Transform.objects.create(**validate_data)
    

class Button_TransitionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Button_Transition
        fields = '__all__' 
    def create(self, validate_data):
         return Button_Transition.objects.create(**validate_data)


class Button_TextSerializer(serializers.ModelSerializer):
    class Meta:
        model= Button_Text
        fields = '__all__' 
    def create(self, validate_data):
         return Button_Text.objects.create(**validate_data)

class Button_AppearanceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Button_Appearance
        fields = '__all__' 
    def create(self, validate_data):
         return Button_Appearance.objects.create(**validate_data)

class Button_ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Button_Action
        fields = '__all__' 
    def create(self, validate_data):
         return Button_Action.objects.create(**validate_data)
    
# Text serializer

class CreateText_Serializer(serializers.ModelSerializer):
     
     class Meta:
        model= Create_Text
        fields = '__all__' 
     def create(self, validate_data):
         return Create_Text.objects.create(**validate_data)
     
class TextTransformSerializer(serializers.ModelSerializer):
    class Meta:
        model= Text_Transform
        fields = '__all__' 
    def create(self, validate_data):
         return Text_Transform.objects.create(**validate_data)

class Text_TransitionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Text_Transition
        fields = '__all__' 
    def create(self, validate_data):
         return Text_Transition.objects.create(**validate_data)
    
class Text_TextSerializer(serializers.ModelSerializer):
    class Meta:
        model= Text_Text
        fields = '__all__' 
    def create(self, validate_data):
         return Text_Text.objects.create(**validate_data)
    
class Text_ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Text_Action
        fields = '__all__' 
    def create(self, validate_data):
         return Text_Action.objects.create(**validate_data)
    
# image serializers 

class ImageDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model= ImageDesign
        fields = '__all__' 
    def create(self, validate_data):
         return ImageDesign.objects.create(**validate_data)

class ImageTransformSerializer(serializers.ModelSerializer):
    class Meta:
        model= Image_Transform
        fields = '__all__' 
    def create(self, validate_data):
         return Image_Transform.objects.create(**validate_data)
    
class Image_TransitionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Image_Transition
        fields = '__all__' 
    def create(self, validate_data):
         return Image_Transition.objects.create(**validate_data)
    
class Image_AppearanceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Image_Appearance
        fields = '__all__' 
    def create(self, validate_data):
         return Image_Appearance.objects.create(**validate_data)

class Image_ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Image_Action
        fields = '__all__' 
    def create(self, validate_data):
         return Image_Action.objects.create(**validate_data)

#video serializers 

class UploadVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model= UploadVideo
        fields = '__all__' 
    def create(self, validate_data):
         return UploadVideo.objects.create(**validate_data)
    
class VideoTransformSerializer(serializers.ModelSerializer):
    class Meta:
        model= Video_Transform
        fields = '__all__' 
    def create(self, validate_data):
         return Video_Transform.objects.create(**validate_data)
    

class Video_TransitionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Video_Transition
        fields = '__all__' 
    def create(self, validate_data):
         return Video_Transition.objects.create(**validate_data)

class Video_ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Video_Action
        fields = '__all__' 
    def create(self, validate_data):
         return Video_Action.objects.create(**validate_data)

# 3D Model serializers

class ThreeDModelFileSerializer(serializers.ModelSerializer):
    class Meta:
        model= ThreeDModelFile
        fields = '__all__' 
    def create(self, validate_data):
         return ThreeDModelFile.objects.create(**validate_data)
    
class ThreeDModel_TransformSerializer(serializers.ModelSerializer):
    class Meta:
        model= ThreeDModel_Transform
        fields = '__all__' 
    def create(self, validate_data):
         return ThreeDModel_Transform.objects.create(**validate_data)


class ThreeDModel_TransitionSerializer(serializers.ModelSerializer):
    class Meta:
        model= ThreeDModel_Transition
        fields = '__all__' 
    def create(self, validate_data):
         return ThreeDModel_Transition.objects.create(**validate_data)

class ThreeDModel_ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model= ThreeDModel_Action
        fields = '__all__' 
    def create(self, validate_data):
         return ThreeDModel_Action.objects.create(**validate_data)
    
# scene serializers

class SceneSerializer(serializers.ModelSerializer):
    class Meta:
        model= Scene
        fields = '__all__' 
    def create(self, validate_data):
         return Scene.objects.create(**validate_data)


class Scene_TransitionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Scene_Transition
        fields = '__all__' 
    def create(self, validate_data):
         return Scene_Transition.objects.create(**validate_data)
    
class Scene_PhotoUISerializer(serializers.ModelSerializer):
    class Meta:
        model= Scene_PhotoUI
        fields = '__all__' 
    def create(self, validate_data):
         return Scene_PhotoUI.objects.create(**validate_data)
    
# project Content Serializers
 
class Project_ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project_Content
        fields = '__all__' 
    def create(self, validate_data):
         return Project_Content.objects.create(**validate_data)
    
class Background_SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model= Background_Sound
        fields = '__all__' 
    def create(self, validate_data):
         return Background_Sound.objects.create(**validate_data)
    
class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Analytics
        fields = '__all__' 
    def create(self, validate_data):
         return Analytics.objects.create(**validate_data)
#2d3dswitch

class TwoD_ThreeD_SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model= TwoD_ThreeD_Switch
        fields = '__all__' 
    def create(self, validate_data):
         return TwoD_ThreeD_Switch.objects.create(**validate_data)
    
# class QRCodeGenerater_Target_imageSerializers(serializers.ModelSerializer):
#      class Meta:
#         model= Target_image_QR_code_image
#         fields = '__all__' 
#      def create(self, validate_data):
#          return Target_image_QR_code_image.objects.create(**validate_data)
    
    
