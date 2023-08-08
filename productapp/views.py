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
url="http://3.109.213.210:8000"
from urllib.parse import urljoin
from django.http import Http404
# background_url="http://127.0.0.1:8000/media/"
background_url="http://3.109.213.210:8000/media/"
# Create button Api 
from productapp.utilities import URLEncrypter
import qrcode 
import sys


class ButtonAPIView(APIView):
    def post(self, request):
        try:
            serializer = ButtonSerializer(data=request.data)
            if serializer.is_valid():
                button = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})
    

    def get_object(self, pk):
        try:
            return Create_Button.objects.get(pk=pk)
        except Create_Button.DoesNotExist:
             raise Http404

    def get(self, request, pk):
        button = self.get_object(pk)
        serializer = ButtonSerializer(button)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        product = self.get_object(pk)
        serializer = ButtonSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Button updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Button_TransformAPIView(APIView):
    def post(self, request):
        serializer = ButtonTransformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ButtonTransformAPIView(APIView):
    def get_object(self, pk):
        try:
            return Button_Transform.objects.get(pk=pk)
        except Button_Transform.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ButtonTransformSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Button Transform updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Button_TransitionAPIView(APIView):
    def post(self, request):
        serializer = Button_TransitionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ButtonTransitionAPIView(APIView):
    def get_object(self, pk):
        try:
            return Button_Transition.objects.get(pk=pk)
        except Button_Transition.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = Button_TransitionSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Button Transition updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Button_TextAPIView(APIView):
    def post(self, request):
        serializer = Button_TextSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ButtonTextAPIView(APIView):
    def get_object(self, pk):
        try:
            return Button_Text.objects.get(pk=pk)
        except Button_Text.DoesNotExist:
            raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = Button_TextSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Button Text updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Button_AppearanceAPIView(APIView):
    def post(self, request):
        serializer = Button_AppearanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ButtonAppearanceAPIView(APIView):
    def get_object(self, pk):
        try:
            return Button_Appearance.objects.get(pk=pk)
        except Button_Appearance.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = Button_AppearanceSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Button Appearance updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Button_ActionAPIView(APIView):
    def post(self, request):
        serializer = Button_ActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ButtonActionAPIView(APIView):
    def get_object(self, pk):
        try:
            return Button_Action.objects.get(pk=pk)
        except Button_Action.DoesNotExist:
            raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = Button_ActionSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Button Action updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class GetButtonData(APIView):
    def get(self, request,pk):
       
       if Create_Button.objects.filter(id=pk).exists():
            array=[]
            Button_data=Create_Button.objects.filter(id=pk).values('Button_name','project_id')
            Button_t = Button_Transform.objects.all().order_by('id')
            serializer1=ButtonTransformSerializer(Button_t,many=True)
            Button_Transform_data={}
            transform_array=[]
            for x in serializer1.data: 
                    
                if pk ==x['button_Id']:
                    Button_Transform_data=x
                    transform_array.append(Button_Transform_data)
            Button_ts = Button_Transition.objects.all().order_by('id')
            serializer2=Button_TransitionSerializer(Button_ts,many=True)
            button_transition_array=[]
            button_transition_data={}
            for y in serializer2.data: 
                    
                if pk ==y['button_Id']:
                    button_transition_data=y
                    button_transition_array.append(button_transition_data)
            Button_txt = Button_Text.objects.all().order_by('id')
            serializer3=Button_TextSerializer(Button_txt,many=True)
            button_text_array=[]
            button_text_data={}
            for z in serializer3.data: 
                    
                if pk ==z['button_Id']:
                    button_text_data=z
                    button_text_array.append(button_text_data)
            Button_ap = Button_Appearance.objects.all().order_by('id')
            serializer4=Button_AppearanceSerializer(Button_ap,many=True)
            button_appearance_array=[]
            button_appearance_data={}
            for i in serializer4.data: 
                if pk ==i['button_Id']:
                    button_appearance_data=i
                    button_appearance_array.append(button_appearance_data)
            Button_act = Button_Action.objects.all().order_by('id')
            serializer5=Button_ActionSerializer(Button_act,many=True)
            button_action_array=[]
            button_action_data={}
            for m in serializer5.data: 
                if pk ==m['button_Id']:
                    button_action_data=m
                    button_action_array.append(button_action_data)
            array=[{"id":pk,"project_id":Button_data[0]['project_id'],"Button_name":Button_data[0]['Button_name'],"Button_Transform":transform_array,"Button_Action":button_action_array,"Button_Transition":button_transition_array,"Button_Text":button_text_array,"button_appearance":button_appearance_array}]
            return Response({"data":array},status=status.HTTP_200_OK)
       else:
             return Response({"message":"Button Not Found"},status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        try:
            Button = Create_Button.objects.get(id=pk)
            Button.delete()

            Button_Transform.objects.filter(button_Id=pk).delete()
            Button_Action.objects.filter(button_Id=pk).delete()
            Button_Transition.objects.filter(button_Id=pk).delete()
            Button_Text.objects.filter(button_Id=pk).delete()
            Button_Appearance.objects.filter(button_Id=pk).delete()

            return Response({"message": "Button data deleted successfully "}, status=status.HTTP_200_OK)
        except Create_Button.DoesNotExist:
            raise Http404
       
#Text Api

class Create_TextAPIView(APIView):
    def post(self, request):
        serializer_class = CreateText_Serializer(data=request.data)
        if serializer_class.is_valid():
            button = serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class Text_TransformAPIView(APIView):
    def post(self, request):
        serializer = TextTransformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TextTransformAPIView(APIView):
    def get_object(self, pk):
        try:
            return Text_Transform.objects.get(pk=pk)
        except Text_Transform.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = TextTransformSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Text transform updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Text_TransitionAPIView(APIView):
    def post(self, request):
        serializer = Text_TransitionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TextTransitionAPIView(APIView):
    def get_object(self, pk):
        try:
            return Text_Transition.objects.get(pk=pk)
        except Text_Transition.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = Text_TransitionSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Text Transition updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Text_TextAPIView(APIView):
    def post(self, request):
        serializer = Text_TextSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TextTextAPIView(APIView):
    def get_object(self, pk):
        try:
            return Text_Text.objects.get(pk=pk)
        except Text_Text.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = Text_TextSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Text  updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Text_ActionAPIView(APIView):
    def post(self, request):
        serializer = Text_ActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TextActionAPIView(APIView):
    def get_object(self, pk):
        try:
            return Text_Action.objects.get(pk=pk)
        except Text_Action.DoesNotExist:
            raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = Text_ActionSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Text Action updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAllTextData(APIView):
    def get(self, request,pk):
     if Create_Text.objects.filter(id=pk).exists():
        array=[]
        Textdata=Create_Text.objects.filter(id=pk).values('Text_name','project_id')
        Text = Text_Transform.objects.all().order_by('id')
        serializer1=TextTransformSerializer(Text,many=True)
        text_transform_array=[]
        Text_Transform_data={}
        for x in serializer1.data: 
                
            if pk ==x['text_id']:
                Text_Transform_data=x
                text_transform_array.append(Text_Transform_data)


        Text2 = Text_Action.objects.all().order_by('id') 
        serializer2=Text_ActionSerializer(Text2,many=True)  
        text_action_array=[]
        Text_Action_data={}
        for y in serializer2.data: 
            
             if pk ==y['text_id']:
                 Text_Action_data=y
                 text_action_array.append(Text_Action_data)

        Text3 = Text_Transition.objects.all().order_by('id') 
        serializer3=Text_TransitionSerializer(Text3,many=True)  
        text_transition_array=[]
        Text_Transition_Data={}
        for i in serializer3.data: 
            if pk ==i['text_id']:
                
                Text_Transition_Data=i
                text_transition_array.append(Text_Transition_Data)
        
        Text4 = Text_Text.objects.all().order_by('id') 
        serializer4=Text_TextSerializer(Text4,many=True)
        text_array=[]
        Text_data={}
        for k in serializer4.data: 
             if pk ==k['text_id']:
                Text_data=k
                text_array.append(Text_data)
        array=[{"id":pk,"Textname":Textdata[0]['Text_name'],"project_id":Textdata[0]['project_id'],"Text_Transform":text_transform_array,"Text_Action":text_action_array,"Text_Transition":text_transition_array,"Text_data":text_array}]
        return Response({"message":"success","data":array},status=status.HTTP_200_OK)
     else:
        return Response({"message":"Data Not Found"},status=status.HTTP_400_BAD_REQUEST)
     
    def delete(self, request, pk):
        try:
            text = Create_Text.objects.get(id=pk)
            text.delete()

            Text_Transform.objects.filter(text_id=pk).delete()
            Text_Action.objects.filter(text_id=pk).delete()
            Text_Transition.objects.filter(text_id=pk).delete()
            Text_Text.objects.filter(text_id=pk).delete()

            return Response({"message": "Text data deleted successfully "}, status=status.HTTP_200_OK)
        except Create_Text.DoesNotExist:
            raise Http404

# Image Api

class UploadImageView(APIView):
    def post(self, request):
        serializer_class = ImageDesignSerializer(data=request.data)
        if serializer_class.is_valid():
            image = serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def get_object(self, pk):
    #     try:
    #         return ImageDesign.objects.get(pk=pk)
    #     except ImageDesign.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk):
    #     image= self.get_object(pk)
    #     serializer = ImageDesignSerializer(image)
    #     full_url = urljoin(url, serializer.data['image'])
    #     data={"id":serializer.data['id'],"image":full_url,"project_id":serializer.data['project_id']}
    #     return Response(data,status=status.HTTP_200_OK)

class Image_TransformAPIView(APIView):
    def post(self, request):
        serializer = ImageTransformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ImageTransformAPIView(APIView):
    def get_object(self, pk):
        try:
            return Image_Transform.objects.get(pk=pk)
        except Image_Transform.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ImageTransformSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Image Transform updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Image_TransitionAPIView(APIView):
    def post(self, request):
        serializer = Image_TransitionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ImageTransitionAPIView(APIView):
    def get_object(self, pk):
        try:
            return Image_Transition.objects.get(pk=pk)
        except Image_Transition.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = Image_TransitionSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Image Transition updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Image_AppearanceAPIView(APIView):
    def post(self, request):
        serializer = Image_AppearanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageAppearanceAPIView(APIView):
    def get_object(self, pk):
        try:
            return Image_Appearance.objects.get(pk=pk)
        except Image_Appearance.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = Image_AppearanceSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Image Appearance updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Image_ActionAPIView(APIView):
    def post(self, request):
        serializer = Image_ActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageActionAPIView(APIView):
    def get_object(self, pk):
        try:
            return Image_Action.objects.get(pk=pk)
        except Image_Action.DoesNotExist:
            raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = Image_ActionSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Image Action updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get all Image Data  
class GetImageDataApiView(APIView):
    def get(self, request,pk):
     if ImageDesign.objects.filter(id=pk).exists():
         array=[]
         Imagedata=ImageDesign.objects.all().order_by('id')
         serializer=ImageDesignSerializer(Imagedata,many=True)
         for i in serializer.data: 
             if pk==i['id']:
                 full_url = urljoin(url,i['image'])
                 project_id=i['project_id']
        
         imaget = Image_Transform.objects.all().order_by('id')
         serializer1=ImageTransformSerializer(imaget,many=True)
         image_transform_array=[]
         Image_Transform_data={}
         for x in serializer1.data: 
            if pk ==x['image_id']:
                Image_Transform_data=x
                image_transform_array.append(Image_Transform_data)
         
         imagetf = Image_Transition.objects.all().order_by('id')
         serializer2=Image_TransitionSerializer(imagetf,many=True)
         image_transition_array=[]
         Image_Transition_data={}
         for z in serializer2.data: 
            if pk ==z['image_id']:
                Image_Transition_data=z
                image_transition_array.append(Image_Transition_data)

         imagetap = Image_Appearance.objects.all().order_by('id')
         serializer3=Image_AppearanceSerializer(imagetap,many=True)
         image_appearance_array=[]
         Image_Appearance_data={}
         for k in serializer3.data: 
            if pk ==k['image_id']:
                Image_Appearance_data=k
                image_appearance_array.append(Image_Appearance_data)
         
         imagetact = Image_Action.objects.all().order_by('id')
         serializer4=Image_ActionSerializer(imagetact,many=True)
         image_action_array=[]
         Image_action_data={}
         for m in serializer4.data: 
            if pk ==m['image_id']:
                Image_action_data=m
                image_action_array.append(Image_action_data)


         array=[{"id":pk,"image":full_url,"project_id":project_id,"Image_Transform":image_transform_array,"Image_Transition":image_transition_array,"Image_Appearance":image_appearance_array,"Image_action":image_action_array}]
       
         return Response({"message":"Success","data":array},status=status.HTTP_200_OK)
     else:
        return Response({"message":"Data Not Found"},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            imagedile = ImageDesign.objects.get(id=pk)
            imagedile.delete()

            Image_Transform.objects.filter(image_id=pk).delete()
            Image_Transition.objects.filter(image_id=pk).delete()
            Image_Appearance.objects.filter(image_id=pk).delete()
            Image_Action.objects.filter(image_id=pk).delete()
        

            return Response({"message": "Image deleted successfully "}, status=status.HTTP_200_OK)
        except ImageDesign.DoesNotExist:
            raise Http404

# video api function

class UploadVideoView(APIView):
    def post(self, request):
        serializer_class = UploadVideoSerializer(data=request.data)
        if serializer_class.is_valid():
            video = serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self, pk):
        try:
            return UploadVideo.objects.get(pk=pk)
        except UploadVideo.DoesNotExist:
           raise Http404

    def get(self, request, pk):
        video= self.get_object(pk)
        serializer = UploadVideoSerializer(video)
        full_url = urljoin(url, serializer.data['video'])
        data={"id":serializer.data['id'],"video_url":full_url,"project_id":serializer.data['project_id']}
        return Response(data,status=status.HTTP_200_OK)

class Video_TransformAPIView(APIView):
    def post(self, request):
        serializer = VideoTransformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VideoTransformAPIView(APIView):
    def get_object(self, pk):
        try:
            return Video_Transform.objects.get(pk=pk)
        except Video_Transform.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = VideoTransformSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Video Transform updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Video_TransitionAPIView(APIView):
    def post(self, request):
        serializer = Video_TransitionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class VideoTransitionAPIView(APIView):
    def get_object(self, pk):
        try:
            return Video_Transition.objects.get(pk=pk)
        except Video_Transition.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = Video_TransitionSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Video Transition updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Video_ActionAPIView(APIView):
    def post(self, request):
        serializer = Video_ActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoActionAPIView(APIView):
    def get_object(self, pk):
        try:
            return Video_Action.objects.get(pk=pk)
        except Video_Action.DoesNotExist:
            raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = Video_ActionSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Video Action updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetVideoDataApiView(APIView):
    def get(self, request,pk):
     if UploadVideo.objects.filter(id=pk).exists():
         array=[]
         Videodata=UploadVideo.objects.all().order_by('id')
         serializer=UploadVideoSerializer(Videodata,many=True)
         for i in serializer.data: 
             if pk==i['id']:
                 full_url = urljoin(url,i['video'])
                 project_id=i['project_id']
        
         Videot = Video_Transform.objects.all().order_by('id')
         serializer1=VideoTransformSerializer(Videot,many=True)
         video_transform_array=[]
         Video_Transform_data={}
         for x in serializer1.data: 
            if pk ==x['video_id']:
                Video_Transform_data=x
                video_transform_array.append(Video_Transform_data)
         
         videotf = Video_Transition.objects.all().order_by('id')
         serializer2=Video_TransitionSerializer(videotf,many=True)
         video_transition_array=[]
         video_Transition_data={}
         for z in serializer2.data: 
            if pk ==z['video_id']:
                video_Transition_data=z
                video_transition_array.append(video_Transition_data)
         
         videotact = Video_Action.objects.all().order_by('id')
         serializer3=Video_ActionSerializer(videotact,many=True)
         video_action_array=[]
         Video_Action_data={}
         for m in serializer3.data: 
            if pk ==m['video_id']:
                Video_Action_data=m
                video_action_array.append(Video_Action_data)

         array=[{"id":pk,"video":full_url,"project_id":project_id,"Video_Transform":video_transform_array,"Video_Transition":video_transition_array,"Video_action":video_action_array}]
       
         return Response({"message":"Success","data":array},status=status.HTTP_200_OK)
     else:
        return Response({"message":"Data Not Found"},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            videofile = UploadVideo.objects.get(id=pk)
            videofile.delete()

            Video_Transform.objects.filter(video_id=pk).delete()
            Video_Transition.objects.filter(video_id=pk).delete()
            Video_Action.objects.filter(video_id=pk).delete()
           
            return Response({"message": "Video deleted successfully "}, status=status.HTTP_200_OK)
        except UploadVideo.DoesNotExist:
            raise Http404

#3d model api functions

class ThreeDModelView(APIView):
    def post(self, request):
        serializer_class = ThreeDModelFileSerializer(data=request.data)
        if serializer_class.is_valid():
            file = serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self, pk):
        try:
            return ThreeDModelFile.objects.get(pk=pk)
        except ThreeDModelFile.DoesNotExist:
           raise Http404

    def get(self, request, pk):
        video= self.get_object(pk)
        serializer = ThreeDModelFileSerializer(video)
        full_url = urljoin(url, serializer.data['File'])
        data={"id":serializer.data['id'],"File_url":full_url,"project_id":serializer.data['project_id']}
        return Response(data,status=status.HTTP_200_OK)

class ThreeDModel_TransformAPIView(APIView):
    def post(self, request):
        serializer = ThreeDModel_TransformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ThreeDModelTransformAPIView(APIView):
    def get_object(self, pk):
        try:
            return ThreeDModel_Transform.objects.get(pk=pk)
        except ThreeDModel_Transform.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ThreeDModel_TransformSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'3D model Transform updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ThreeDModel_TransitionAPIView(APIView):
    def post(self, request):
        serializer = ThreeDModel_TransitionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ThreeDModelTransitionAPIView(APIView):
    def get_object(self, pk):
        try:
            return ThreeDModel_Transition.objects.get(pk=pk)
        except ThreeDModel_Transition.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ThreeDModel_TransitionSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'3D model Transition updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ThreeDModel_ActionAPIView(APIView):
    def post(self, request):
        serializer = ThreeDModel_ActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ThreeDModelActionAPIView(APIView):
    def get_object(self, pk):
        try:
            return ThreeDModel_Action.objects.get(pk=pk)
        except ThreeDModel_Action.DoesNotExist:
            raise Http404


    
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ThreeDModel_ActionSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'3D model action updated  successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class GetThreeDModelDataView(APIView):
    def get(self, request,pk):
     if ThreeDModelFile.objects.filter(id=pk).exists():
         array=[]
         threeddata=ThreeDModelFile.objects.all().order_by('id')
         serializer=ThreeDModelFileSerializer(threeddata,many=True)
         for i in serializer.data: 
             if pk==i['id']:
                 full_url = urljoin(url,i['File'])
                 project_id=i['project_id']
               
        
         threedt = ThreeDModel_Transform.objects.all().order_by('id')
         serializer1=ThreeDModel_TransformSerializer(threedt,many=True)
         threeDModel_Transform_array=[]
         threeDModel_Transform_data={}
         for x in serializer1.data: 
            if pk ==x['ThreeDModel_id']:
                threeDModel_Transform_data=x
                threeDModel_Transform_array.append(threeDModel_Transform_data)
         
         threedtf = ThreeDModel_Transition.objects.all().order_by('id')
         serializer2=ThreeDModel_TransitionSerializer(threedtf,many=True)
         threeDModel_Transition_array=[]
         threeDModel_Transition_data={}
         for z in serializer2.data: 
            if pk ==z['ThreeDModel_id']:
                threeDModel_Transition_data=z
                threeDModel_Transition_array.append(threeDModel_Transition_data)
         
         threedtact = ThreeDModel_Action.objects.all().order_by('id')
         serializer3=ThreeDModel_ActionSerializer(threedtact,many=True)
         threed_Action_array=[]
         threed_Action_data={}
         for m in serializer3.data: 
            if pk ==m['ThreeDModel_id']:
                threed_Action_data=m
                threed_Action_array.append(threed_Action_data)

         array=[{"id":pk,"file":full_url,"project_id":project_id,"ThreeD_Transform":threeDModel_Transform_array,"threeDModel_Transition":threeDModel_Transition_array,"threed_action":threed_Action_array}]
       
         return Response({"message":"Success","data":array},status=status.HTTP_200_OK)
     else:
        return Response({"message":"Data Not Found"},status=status.HTTP_400_BAD_REQUEST)
     
    def delete(self, request, pk):
        try:
            threeDmodel = ThreeDModelFile.objects.get(id=pk)
            threeDmodel.delete()

            ThreeDModel_Transform.objects.filter(ThreeDModel_id=pk).delete()
            ThreeDModel_Transition.objects.filter(ThreeDModel_id=pk).delete()
            ThreeDModel_Action.objects.filter(ThreeDModel_id=pk).delete()
           
            return Response({"message": "3D model file deleted  successfully "}, status=status.HTTP_200_OK)
        except ThreeDModelFile.DoesNotExist:
            raise Http404
    
#  Scene Api class Functions
class SceneApiView(APIView):
    def post(self, request):
        serializer_class = SceneSerializer(data=request.data)
        if serializer_class.is_valid():
            file = serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class Scene_APIView(APIView):
    def get_object(self, pk):
        try:
            return Scene.objects.get(pk=pk)
        except Scene.DoesNotExist:
            raise Http404
    
    # def get(self, request, pk):
    #     scene = self.get_object(pk)
    #     serializer = SceneSerializer(scene)
    #     return Response(serializer.data)

    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = SceneSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Scene updated  successfully','data':serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Scene_TransitionAPIView(APIView):
    def post(self, request):
        serializer = Scene_TransitionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SceneTransitionAPIView(APIView):
    def get_object(self, pk):
        try:
            return Scene_Transition.objects.get(pk=pk)
        except Scene_Transition.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = Scene_TransitionSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Scene Transition updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScenePhotoUI_APIView(APIView):
    def post(self, request):
        serializer = Scene_PhotoUISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ScenePhotoUIAPIView(APIView):
    def get_object(self, pk):
        try:
            return Scene_PhotoUI.objects.get(pk=pk)
        except Scene_PhotoUI.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = Scene_PhotoUISerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Scene PhotoUI updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetSceneData(APIView):
    def get(self, request,pk):
     if Scene.objects.filter(id=pk).exists():
         array=[]
         sceneddata=Scene.objects.all().order_by('id')
         serializer=SceneSerializer(sceneddata,many=True)
         for i in serializer.data: 
             if pk==i['id']:
                 scene_name = i['name']
                 project_id=i['project_id']
          
         scenetf = Scene_Transition.objects.all().order_by('id')
         serializer2=Scene_TransitionSerializer(scenetf,many=True)
         scene_Transition_array=[]
         scene_Transition_data={}
         for z in serializer2.data: 
            if pk ==z['scene_id']:
                scene_Transition_data=z
                scene_Transition_array.append(scene_Transition_data)
         
         scenephoto_ui_d = Scene_PhotoUI.objects.all().order_by('id')
         serializer3=Scene_PhotoUISerializer(scenephoto_ui_d,many=True)
         scenephoto_ui_array=[]
         scenephoto_ui_data={}
         for m in serializer3.data: 
            if pk ==m['scene_id']:
                scenephoto_ui_data=m
                scenephoto_ui_array.append(scenephoto_ui_data)

         array=[{"id":pk,"name":scene_name,"project_id":project_id,"Scene_Transition":scene_Transition_array,"Scene_PhotoUI":scenephoto_ui_array}]
       
         return Response({"message":"Success","data":array},status=status.HTTP_200_OK)
     else:
        return Response({"message":"Data Not Found"},status=status.HTTP_400_BAD_REQUEST)
     
    def delete(self, request, pk):
        try:
            scenedata = Scene.objects.get(id=pk)
            scenedata.delete()

            Scene_Transition.objects.filter(scene_id=pk).delete()
            Scene_PhotoUI.objects.filter(scene_id=pk).delete()
            return Response({"message":"scene deleted  successfully"}, status=status.HTTP_200_OK)
        except Scene.DoesNotExist:
            raise Http404

# project Content api class Function

class ProjectContent_APIView(APIView):
    def post(self, request):
        serializer = Project_ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProjectContentAPIView(APIView):
    def get_object(self, pk):
        try:
            return Project_Content.objects.get(pk=pk)
        except Project_Content.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = Project_ContentSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            target_image=urljoin(url,serializer.data['target_image'])
            return Response({'message':'project content updated successfully','data':target_image})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Background_SoundAPIView(APIView):
    def post(self, request):
        serializer = Background_SoundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BackgroundSoundAPIView(APIView):
    def get_object(self, pk):
        try:
            return Background_Sound.objects.get(pk=pk)
        except Background_Sound.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = Background_SoundSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'background sound updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Analytics_APIView(APIView):
    def post(self, request):
        serializer = AnalyticsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AnalyticsAPIView(APIView):
    def get_object(self, pk):
        try:
            return Analytics.objects.get(pk=pk)
        except Analytics.DoesNotExist:
             raise Http404
    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = AnalyticsSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Analytics updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetProjectContentData(APIView):
    def get(self, request,pk):
     if Project_Content.objects.filter(id=pk).exists():
         array=[]
         project_content_d=Project_Content.objects.all().order_by('id')
         serializer=Project_ContentSerializer(project_content_d,many=True)
         project_content_array=[]
         scenproject_content_data={}
         for i in serializer.data: 
             if pk==i['id']:
                 full_url=urljoin(url,i['target_image'])
                 scenproject_content_data ={"id":i['id'],"opacity":i['opacity'],"orientation":i['orientation'],
                                            "dimensions_w":i['dimensions_w'],"dimensions_h":i['dimensions_h'],
                                            "units":i['units'],"project_Id":i['project_Id'],"target_image":full_url}
                 project_content_array.append(scenproject_content_data)
    
         back_data = Background_Sound.objects.all().order_by('id')
         serializer2=Background_SoundSerializer(back_data,many=True)
         background_sound_array=[]
         background_sound_data={}
         for z in serializer2.data: 
            if pk ==z['project_content_id']:
                full_url1=urljoin(url,z['media_file'])
                background_sound_data={"id":i['id'],"media_file":full_url1,"project_content_id":z['project_content_id']}
                background_sound_array.append(background_sound_data)
         analytics_d = Analytics.objects.all().order_by('id')
         serializer3=AnalyticsSerializer(analytics_d,many=True)
         analytics_array=[]
         analytics_data={}
         for m in serializer3.data: 
            if pk ==m['project_content_id']:
                analytics_data=m
                analytics_array.append(analytics_data)

         array=[{"Project_Content":project_content_array,"Background_Sound":background_sound_array,"analytics":analytics_array}]
       
         return Response({"message":"Success","data":array},status=status.HTTP_200_OK)
     else:
        return Response({"message":"Data Not Found"},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            priojectcontent = Project_Content.objects.get(id=pk)
            priojectcontent.delete()

            Background_Sound.objects.filter(project_content_id=pk).delete()
            Analytics.objects.filter(project_content_id=pk).delete()
            return Response({"message":"project data deleted  successfully"}, status=status.HTTP_200_OK)
        except Project_Content.DoesNotExist:
            raise Http404

#2d3d switch api functions

class TwoD_ThreeD_Switch_APIView(APIView):
    def post(self, request):
        serializer = TwoD_ThreeD_SwitchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from cryptography.fernet import Fernet

class TwoD_ThreeDSwitchAPIView(APIView):
    
    def get_object(self, pk):
        try:
            return TwoD_ThreeD_Switch.objects.get(pk=pk)
        except TwoD_ThreeD_Switch.DoesNotExist:
             raise Http404
        
    
    @csrf_exempt
    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = TwoD_ThreeD_SwitchSerializer(product)
        return Response(serializer.data)


    @csrf_exempt
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = TwoD_ThreeD_SwitchSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectAllDetailById(APIView):
    def get(self, request,pk):
        array=[]
        if CreateProject.objects.filter(id=pk).exists():
            button=Create_Button.objects.all().order_by('id')
            serializer_class=ButtonSerializer(button,many=True)
            button_array=[]
            for createbuttondata in serializer_class.data:
                project_id=createbuttondata['project_id']
                if project_id==pk:
                    button_id=createbuttondata['id']
                    button_name=createbuttondata['Button_name']
                    button_transform=list(Button_Transform.objects.filter(button_Id=button_id).values())
                    button_transition=list(Button_Transition.objects.filter(button_Id=button_id).values())
                    button_text=list(Button_Text.objects.filter(button_Id=button_id).values())
                    button_appearance=list(Button_Appearance.objects.filter(button_Id=button_id).values())
                    button_action=list(Button_Action.objects.filter(button_Id=button_id).values())
                    button_transition_dict = button_transition[0] if button_transition else {}
                    button_transform_dict = button_transform[0] if button_transform else {}
                    button_text_dict = button_text[0] if button_text else {}
                    button_appearance_dict = button_appearance[0] if button_appearance else {}
                    button_action_dict = button_action[0] if button_action else {}
                    button_dict_array = [
                        {
                        "button_id":button_id,
                        "button_name":button_name,  
                        "button_transition": button_transition_dict,
                        "button_transform": button_transform_dict,
                        "button_text": button_text_dict,
                        "button_appearance": button_appearance_dict,
                        "button_action": button_action_dict}]
                    
                    
                    button_array.append(button_dict_array)
            
            text=Create_Text.objects.all().order_by('id')
            serializer_class1=CreateText_Serializer(text,many=True)
            text_array=[]
            for create_text_data in serializer_class1.data:
                project_id=create_text_data['project_id']
                if project_id==pk:
                    text_name=create_text_data['Text_name']
                    text_id=create_text_data['id']
                    text_transform=list(Text_Transform.objects.filter(text_id=text_id).values())
                    text_action=list(Text_Action.objects.filter(text_id=text_id).values())
                    text_transition=list(Text_Transition.objects.filter(text_id=text_id).values())
                    text_text=list(Text_Text.objects.filter(text_id=text_id).values())
                    text_transform_dict = text_transform[0] if text_transform else {}
                    text_action_dict = text_action[0] if text_action else {}
                    text_transition_dict = text_transition[0] if text_transition else {}
                    text_text_dict = text_text[0] if text_text else {}
                    text_dict_array = [
                        {
                        "text_id":text_id,
                        "button_name":text_name,  
                        "text_transition": text_transition_dict,
                        "text_transform": text_transform_dict,
                        "text_text": text_text_dict,
                        "text_action": text_action_dict}]
                    text_array.append(text_dict_array)
            image=ImageDesign.objects.all().order_by('id')
            serializer_class2=ImageDesignSerializer(image,many=True)
            image_array=[]
            for image_data in serializer_class2.data:
                project_id=image_data['project_id']
                if project_id==pk:
                    image_id=image_data['id']
                    image_url = urljoin(url,image_data['image'])
                    image_transform=list(Image_Transform.objects.filter(image_id=image_id).values())
                    image_appearance=list(Image_Appearance.objects.filter(image_id=image_id).values())
                    image_action=list(Image_Action.objects.filter(image_id=image_id).values())
                    image_transition=list(Image_Transition.objects.filter(image_id=image_id).values())
                    image_transform_dict = image_transform[0] if image_transform else {}
                    image_appearance_dict = image_appearance[0] if image_appearance else {}
                    image_action_dict = image_action[0] if image_action else {}
                    image_transition_dict = image_transition[0] if image_transition else {}
                    image_dict_array = [
                        {
                        "image_id":image_id,
                        "image_url":image_url,  
                        "image_transform": image_transform_dict,
                        "image_appearance": image_appearance_dict,
                        "image_action": image_action_dict,
                        "image_transition":image_transition_dict}]
                    image_array.append(image_dict_array)
                   
         
            video=UploadVideo.objects.all().order_by('id')
            serializer_class3=UploadVideoSerializer(video,many=True)
            video_array=[]
            for video_data in serializer_class3.data:
                project_id=video_data['project_id']
                if project_id==pk:
                    video_id=video_data['id']
                    video_url=urljoin(url,video_data['video'])
                    video_transform=list(Video_Transform.objects.filter(video_id=video_id).values())
                    video_action=list(Video_Action.objects.filter(video_id=video_id).values())
                    video_transition=list(Video_Transition.objects.filter(video_id=video_id).values())
                    video_transform_dict = video_transform[0] if video_transform else {}
                    video_action_dict = video_action[0] if video_action else {}
                    video_transition_dict = video_transition[0] if video_transition else {}
                    video_dict_array = [
                        {
                        "video_id":video_id,
                        "video_url":video_url,  
                        "video_transform": video_transform_dict,
                        "video_transition": video_transition_dict,
                        "video_action": video_action_dict,
                        }]
                    video_array.append(video_dict_array)
            
            threed=ThreeDModelFile.objects.all().order_by('id')
            serializer_class4=ThreeDModelFileSerializer(threed,many=True)
            threed_array=[]
            for threed_data in serializer_class4.data:
                project_id=threed_data['project_id']
                if project_id==pk:
                    threed_id=threed_data['id']
                    file_url=urljoin(url,threed_data['File'])
                    threedModel_transform=list(ThreeDModel_Transform.objects.filter(ThreeDModel_id=threed_id).values())
                    threedModel_action=list(ThreeDModel_Action.objects.filter(ThreeDModel_id=threed_id).values())
                    threedModel_transition=list(ThreeDModel_Transition.objects.filter(ThreeDModel_id=threed_id).values())
                    threedModel_transform_dict = threedModel_transform[0] if threedModel_transform else {}
                    threedModel_action_dict = threedModel_action[0] if threedModel_action else {}
                    threedModel_transition_dict = threedModel_transition[0] if threedModel_transition else {}
                    threed_dict_array = [
                        {
                        "threed_id":threed_id,
                        "file_url":file_url,  
                        "threedModel_transform": threedModel_transform_dict,
                        "threedModel_transition":threedModel_transition_dict ,
                        "threedModel_action": threedModel_action_dict,
                        }]
                    threed_array.append(threed_dict_array)
            scene=Scene.objects.all().order_by('id')
            serializer_class5=SceneSerializer(scene,many=True)
            scene_array=[]
            for scene_data in serializer_class5.data:
                project_id=scene_data['project_id']
                if project_id==pk:
                    scene_id=scene_data['id']
                    scene_name=scene_data['name']
                    scene_transition=list(Scene_Transition.objects.filter(scene_id=scene_id).values())
                    scene_photoUI=list(Scene_PhotoUI.objects.filter(scene_id=scene_id).values())
                    scene_transition_dict = scene_transition[0] if scene_transition else {}
                    scene_photoUI_dict = scene_photoUI[0] if scene_photoUI else {}
                    scene_dict_array = [
                        {
                        "scene_id":scene_id,
                        "scene_name":scene_name,  
                        "scene_transition": scene_transition_dict,
                        "scene_photoUI":scene_photoUI_dict ,
                        }]
                    scene_array.append(scene_dict_array)
            project_content=Project_Content.objects.all().order_by('id')
            serializer_class6=Project_ContentSerializer(project_content,many=True)
            project_content_array=[]
            for project_content_data in serializer_class6.data:
                project_id=project_content_data['project_Id']
                if project_id==pk:
                    project_conten_id=project_content_data['id']
                    opacity=project_content_data['opacity']
                    orientation=project_content_data['orientation']
                    target_image=project_content_data['target_image']
                    
                    if not target_image:
                        target_image=None
                    else:

                        target_image=urljoin(url,project_content_data['target_image'])
                    dimensions_w=project_content_data['dimensions_w']
                    dimensions_h=project_content_data['dimensions_h']
                    units=project_content_data['units']
                    background_sound=list(Background_Sound.objects.filter(project_content_id=project_conten_id).values())
                    analytics=list(Analytics.objects.filter(project_content_id=project_conten_id).values())
                    # print('media file---->',background_sound[0]['media_file'])
                    if not background_sound[0]['media_file']:
                        background_sound[0]['media_file']=None
                    else:
                        background_sound[0]['media_file']=urljoin(background_url,background_sound[0]['media_file'])
                    background_sound_dict = background_sound[0]={'id':background_sound[0]['id'],'media_file':background_sound[0]['media_file'],'project_content_id':project_conten_id} if background_sound else {}
                    background_sound[0]
                    analytics_dict = analytics[0] if analytics else {}
                    projectcontent_dict_array = [
                        {
                        "project_content_id":project_conten_id,
                        "opacity":opacity,  
                        "target_image": target_image,
                        "orientation":orientation ,
                        "dimensions_w":dimensions_w,
                        "dimensions_h":dimensions_h,
                        "units":units,
                        "background_sound":background_sound_dict,
                        "analytics_dict":analytics_dict

                        }]
                    project_content_array.append(projectcontent_dict_array)
            array=[{"project_id":pk,"button_data":button_array,"text_data":text_array,"image_data":image_array,"video_data":video_array,"ThreeDmodeldata":threed_array,"scene_data":scene_array,"project_content_data":project_content_array}]
            return Response({"message":"success","data":array},status=status.HTTP_200_OK)
        else:
            return Response({"message":"Data Not Found"},status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            project = get_object_or_404(CreateProject, id=pk)
        
            Create_Button.objects.filter(project_id=pk).delete()

            Button_Transition.objects.filter(button_Id__in=Create_Button.objects.filter(project_id=pk).values('id')).delete()
            Button_Transition.objects.filter(button_Id__in=Create_Button.objects.filter(project_id=pk).values('id')).delete()
            Button_Text.objects.filter(button_Id__in=Create_Button.objects.filter(project_id=pk).values('id')).delete()
            Button_Appearance.objects.filter(button_Id__in=Create_Button.objects.filter(project_id=pk).values('id')).delete()
            Button_Action.objects.filter(button_Id__in=Create_Button.objects.filter(project_id=pk).values('id')).delete()

            Create_Text.objects.filter(project_id=pk).delete()

            Text_Transform.objects.filter(text_id__in=Create_Text.objects.filter(project_id=pk).values('id')).delete()
            Text_Action.objects.filter(text_id__in=Create_Text.objects.filter(project_id=pk).values('id')).delete()
            Text_Transition.objects.filter(text_id__in=Create_Text.objects.filter(project_id=pk).values('id')).delete()
            Text_Text.objects.filter(text_id__in=Create_Text.objects.filter(project_id=pk).values('id')).delete()
            
            ImageDesign.objects.filter(project_id=pk).delete()
            Image_Transform.objects.filter(image_id__in=ImageDesign.objects.filter(project_id=pk).values('id')).delete()
            Image_Appearance.objects.filter(image_id__in=ImageDesign.objects.filter(project_id=pk).values('id')).delete()
            Image_Action.objects.filter(image_id__in=ImageDesign.objects.filter(project_id=pk).values('id')).delete()
            Image_Transition.objects.filter(image_id__in=ImageDesign.objects.filter(project_id=pk).values('id')).delete()

            UploadVideo.objects.filter(project_id=pk).delete()
            Video_Transform.objects.filter(video_id__in=UploadVideo.objects.filter(project_id=pk).values('id')).delete()
            Video_Action.objects.filter(video_id__in=UploadVideo.objects.filter(project_id=pk).values('id')).delete()
            Video_Transition.objects.filter(video_id__in=UploadVideo.objects.filter(project_id=pk).values('id')).delete()

            ThreeDModelFile.objects.filter(project_id=pk).delete()
            ThreeDModel_Transform.objects.filter(ThreeDModel_id__in=ThreeDModelFile.objects.filter(project_id=pk).values('id')).delete()
            ThreeDModel_Action.objects.filter(ThreeDModel_id__in=ThreeDModelFile.objects.filter(project_id=pk).values('id')).delete()
            ThreeDModel_Transition.objects.filter(ThreeDModel_id__in=ThreeDModelFile.objects.filter(project_id=pk).values('id')).delete()

            Scene.objects.filter(project_id=pk).delete()
            Scene_Transition.objects.filter(scene_id__in=Scene.objects.filter(project_id=pk).values('id')).delete()
            Scene_PhotoUI.objects.filter(scene_id__in=Scene.objects.filter(project_id=pk).values('id')).delete()

            Project_Content.objects.filter(project_Id=pk).delete()
            Background_Sound.objects.filter(project_content_id__in=Project_Content.objects.filter(project_Id=pk).values('id')).delete()
            Analytics.objects.filter(project_content_id__in=Project_Content.objects.filter(project_Id=pk).values('id')).delete()
        
            project.delete()

           
            return Response({"message":"project data deleted  successfully"}, status=status.HTTP_200_OK)
        except Project_Content.DoesNotExist:
            raise Http404


class SceneAllDetailById(APIView):
    def get(self, request,pk):
        array=[]
        if Scene.objects.filter(id=pk).exists():

            scene=Scene.objects.all().order_by('id')
            serializer_class5=SceneSerializer(scene,many=True)
            scene_array=[]
            for scene_data in serializer_class5.data:
                scene_id=scene_data['id']
                scene_name=scene_data['name']
                FeaturedtrackerOption=scene_data['FeaturedtrackerOption']
                if scene_id==pk:
                    scene_transition=list(Scene_Transition.objects.filter(scene_id=scene_id).values())
                    scene_photoUI=list(Scene_PhotoUI.objects.filter(scene_id=scene_id).values())
                    scene_transition_dict = scene_transition[0] if scene_transition else {}
                    scene_photoUI_dict = scene_photoUI[0] if scene_photoUI else {}
                    scene_dict_array = [
                        {
                        "scene_name":scene_name,
                        "FeaturedtrackerOption":FeaturedtrackerOption,
                        "scene_transition": scene_transition_dict,
                        "scene_photoUI":scene_photoUI_dict ,
                        }]
                    scene_array.append(scene_dict_array)

            button=Create_Button.objects.all().order_by('id')
            serializer_class=ButtonSerializer(button,many=True)
            button_array=[]
            for createbuttondata in serializer_class.data:
                scene_id=createbuttondata['scene_id']
                if scene_id==pk:
                    button_id=createbuttondata['id']
                    button_name=createbuttondata['Button_name']
                    button_transform=list(Button_Transform.objects.filter(button_Id=button_id).values())
                    button_transition=list(Button_Transition.objects.filter(button_Id=button_id).values())
                    button_text=list(Button_Text.objects.filter(button_Id=button_id).values())
                    button_appearance=list(Button_Appearance.objects.filter(button_Id=button_id).values())
                    button_action=list(Button_Action.objects.filter(button_Id=button_id).values())
                    button_transition_dict = button_transition[0] if button_transition else {}
                    button_transform_dict = button_transform[0] if button_transform else {}
                    button_text_dict = button_text[0] if button_text else {}
                    button_appearance_dict = button_appearance[0] if button_appearance else {}
                    button_action_dict = button_action[0] if button_action else {}
                    button_dict_array = [
                        {
                        "button_id":button_id,
                        "button_name":button_name,  
                        "button_transition": button_transition_dict,
                        "button_transform": button_transform_dict,
                        "button_text": button_text_dict,
                        "button_appearance": button_appearance_dict,
                        "button_action": button_action_dict}]
                    
                    
                    button_array.append(button_dict_array)
            
            text=Create_Text.objects.all().order_by('id')
            serializer_class1=CreateText_Serializer(text,many=True)
            text_array=[]
            for create_text_data in serializer_class1.data:
                scene_id=create_text_data['scene_id']
                if scene_id==pk:
                    text_name=create_text_data['Text_name']
                    text_id=create_text_data['id']
                    text_transform=list(Text_Transform.objects.filter(text_id=text_id).values())
                    text_action=list(Text_Action.objects.filter(text_id=text_id).values())
                    text_transition=list(Text_Transition.objects.filter(text_id=text_id).values())
                    text_text=list(Text_Text.objects.filter(text_id=text_id).values())
                    text_transform_dict = text_transform[0] if text_transform else {}
                    text_action_dict = text_action[0] if text_action else {}
                    text_transition_dict = text_transition[0] if text_transition else {}
                    text_text_dict = text_text[0] if text_text else {}
                    text_dict_array = [
                        {
                        "text_id":text_id,
                        "button_name":text_name,  
                        "text_transition": text_transition_dict,
                        "text_transform": text_transform_dict,
                        "text_text": text_text_dict,
                        "text_action": text_action_dict}]
                    text_array.append(text_dict_array)
            
            image=ImageDesign.objects.all().order_by('id')
            serializer_class2=ImageDesignSerializer(image,many=True)
            image_array=[]
            for image_data in serializer_class2.data:
                scene_id=image_data['scene_id']
                if scene_id==pk:
                    image_id=image_data['id']
                    image_url = urljoin(url,image_data['image'])
                    image_transform=list(Image_Transform.objects.filter(image_id=image_id).values())
                    image_appearance=list(Image_Appearance.objects.filter(image_id=image_id).values())
                    image_action=list(Image_Action.objects.filter(image_id=image_id).values())
                    image_transition=list(Image_Transition.objects.filter(image_id=image_id).values())
                    image_transform_dict = image_transform[0] if image_transform else {}
                    image_appearance_dict = image_appearance[0] if image_appearance else {}
                    image_action_dict = image_action[0] if image_action else {}
                    image_transition_dict = image_transition[0] if image_transition else {}
                    image_dict_array = [
                        {
                        "image_id":image_id,
                        "image_url":image_url,  
                        "image_transform": image_transform_dict,
                        "image_appearance": image_appearance_dict,
                        "image_action": image_action_dict,
                        "image_transition":image_transition_dict}]
                    image_array.append(image_dict_array)
            
            video=UploadVideo.objects.all().order_by('id')
            serializer_class3=UploadVideoSerializer(video,many=True)
            video_array=[]
            for video_data in serializer_class3.data:
                scene_id=video_data['scene_id']
                if scene_id==pk:
                    video_id=video_data['id']
                    video_url=urljoin(url,video_data['video'])
                    video_transform=list(Video_Transform.objects.filter(video_id=video_id).values())
                    video_action=list(Video_Action.objects.filter(video_id=video_id).values())
                    video_transition=list(Video_Transition.objects.filter(video_id=video_id).values())
                    video_transform_dict = video_transform[0] if video_transform else {}
                    video_action_dict = video_action[0] if video_action else {}
                    video_transition_dict = video_transition[0] if video_transition else {}
                    video_dict_array = [
                        {
                        "video_id":video_id,
                        "video_url":video_url,  
                        "video_transform": video_transform_dict,
                        "video_transition": video_transition_dict,
                        "video_action": video_action_dict,
                        }]
                    video_array.append(video_dict_array)
            threed=ThreeDModelFile.objects.all().order_by('id')
            serializer_class4=ThreeDModelFileSerializer(threed,many=True)
            threed_array=[]
            for threed_data in serializer_class4.data:
                scene_id=threed_data['scene_id']
                if scene_id==pk:
                    threed_id=threed_data['id']
                    file_url=urljoin(url,threed_data['File'])
                    threedModel_transform=list(ThreeDModel_Transform.objects.filter(ThreeDModel_id=threed_id).values())
                    threedModel_action=list(ThreeDModel_Action.objects.filter(ThreeDModel_id=threed_id).values())
                    threedModel_transition=list(ThreeDModel_Transition.objects.filter(ThreeDModel_id=threed_id).values())
                    threedModel_transform_dict = threedModel_transform[0] if threedModel_transform else {}
                    threedModel_action_dict = threedModel_action[0] if threedModel_action else {}
                    threedModel_transition_dict = threedModel_transition[0] if threedModel_transition else {}
                    threed_dict_array = [
                        {
                        "threed_id":threed_id,
                        "file_url":file_url,  
                        "threedModel_transform": threedModel_transform_dict,
                        "threedModel_transition":threedModel_transition_dict ,
                        "threedModel_action": threedModel_action_dict,
                        }]
                    threed_array.append(threed_dict_array)
            array=[{"id":pk,"scene_data":scene_array,"button_data":button_array,"text_data":text_array,"image_data":image_array,"video_data":video_array,"ThreeDmodeldata":threed_array}]
            return Response({"message":"Success","data":array},status=status. HTTP_200_OK)
        else:
            return Response({"message":"Data Not Found"},status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        try:
            scene = get_object_or_404(Scene, id=pk)
        
            Scene.objects.filter(id=pk).delete()
            Scene_Transition.objects.filter(scene_id__in=Scene.objects.filter(id=pk).values('id')).delete()
            Scene_PhotoUI.objects.filter(scene_id__in=Scene.objects.filter(id=pk).values('id')).delete()
            
            Create_Button.objects.filter(scene_id=pk).delete()
            Button_Transition.objects.filter(button_Id__in=Create_Button.objects.filter(scene_id=pk).values('id')).delete()
            Button_Transition.objects.filter(button_Id__in=Create_Button.objects.filter(scene_id=pk).values('id')).delete()
            Button_Text.objects.filter(button_Id__in=Create_Button.objects.filter(scene_id=pk).values('id')).delete()
            Button_Appearance.objects.filter(button_Id__in=Create_Button.objects.filter(scene_id=pk).values('id')).delete()
            Button_Action.objects.filter(button_Id__in=Create_Button.objects.filter(scene_id=pk).values('id')).delete()

            Create_Text.objects.filter(scene_id=pk).delete()

            Text_Transform.objects.filter(text_id__in=Create_Text.objects.filter(scene_id=pk).values('id')).delete()
            Text_Action.objects.filter(text_id__in=Create_Text.objects.filter(scene_id=pk).values('id')).delete()
            Text_Transition.objects.filter(text_id__in=Create_Text.objects.filter(scene_id=pk).values('id')).delete()
            Text_Text.objects.filter(text_id__in=Create_Text.objects.filter(scene_id=pk).values('id')).delete()
            
            ImageDesign.objects.filter(scene_id=pk).delete()
            Image_Transform.objects.filter(image_id__in=ImageDesign.objects.filter(scene_id=pk).values('id')).delete()
            Image_Appearance.objects.filter(image_id__in=ImageDesign.objects.filter(scene_id=pk).values('id')).delete()
            Image_Action.objects.filter(image_id__in=ImageDesign.objects.filter(scene_id=pk).values('id')).delete()
            Image_Transition.objects.filter(image_id__in=ImageDesign.objects.filter(scene_id=pk).values('id')).delete()

            UploadVideo.objects.filter(scene_id=pk).delete()
            Video_Transform.objects.filter(video_id__in=UploadVideo.objects.filter(scene_id=pk).values('id')).delete()
            Video_Action.objects.filter(video_id__in=UploadVideo.objects.filter(scene_id=pk).values('id')).delete()
            Video_Transition.objects.filter(video_id__in=UploadVideo.objects.filter(scene_id=pk).values('id')).delete()

            ThreeDModelFile.objects.filter(scene_id=pk).delete()
            ThreeDModel_Transform.objects.filter(ThreeDModel_id__in=ThreeDModelFile.objects.filter(scene_id=pk).values('id')).delete()
            ThreeDModel_Action.objects.filter(ThreeDModel_id__in=ThreeDModelFile.objects.filter(scene_id=pk).values('id')).delete()
            ThreeDModel_Transition.objects.filter(ThreeDModel_id__in=ThreeDModelFile.objects.filter(scene_id=pk).values('id')).delete()

            scene.delete()

            return Response({"message":"scene data deleted  successfully"}, status=status.HTTP_200_OK)
        
        except Scene.DoesNotExist:
            raise Http404


class GetSceneByProjectId(APIView):
    def get(self, request, pk):
        scenes = Scene.objects.filter(project_id=pk).order_by('id')
        serializer = SceneSerializer(scenes, many=True)
        
        project_content = Project_Content.objects.filter(project_id=pk).order_by('id')
        project_content_serializer = Project_ContentSerializer(project_content, many=True)
        
        background_sound = Background_Sound.objects.filter(project_content_id__in=project_content).order_by('id')
        background_sound_serializer = Background_SoundSerializer(background_sound, many=True)
        
        analytics = Analytics.objects.filter(project_content_id__in=project_content).order_by('id')
        analytics_serializer = AnalyticsSerializer(analytics, many=True)
        
        if scenes.exists() or project_content.exists() or background_sound.exists() or analytics.exists():
            data = {
                'scenes': serializer.data,
                'project_content': [
                    {
                        'id': pc['id'],
                        'opacity': pc['opacity'],
                        'target_image': urljoin(url, pc['target_image']) if pc['target_image'] else None,
                        'orientation': pc['orientation'],
                        'dimensions_w': pc['dimensions_w'],
                        'dimensions_h': pc['dimensions_h'],
                        'units': pc['units'],
                    } for pc in project_content_serializer.data
                ],
                'background_sound': [
                    {
                        'project_content_id': bs['project_content_id'],
                        'media_file':urljoin(url, bs['media_file']) if bs['media_file'] else None,
                        
                    } for bs in background_sound_serializer.data
                ],
                'analytics': analytics_serializer.data
            }
        else:

            data = {'data':'No data found'}

        return Response(data)



class UserDataAPIView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)

            create_projects = user.createproject_set.all()

            image_designs = ImageDesign.objects.filter(scene_id__project_id__in=create_projects)
            upload_videos = UploadVideo.objects.filter(scene_id__project_id__in=create_projects)
            three_d_model_files = ThreeDModelFile.objects.filter(scene_id__project_id__in=create_projects)

            image_design_serializer = ImageDesignSerializer(image_designs, many=True)
            upload_video_serializer = UploadVideoSerializer(upload_videos, many=True)
            three_d_model_file_serializer = ThreeDModelFileSerializer(three_d_model_files, many=True)
            
            image_array=[]
            for images_data in image_design_serializer.data:
                image_id=images_data['id']
                image=urljoin(url,(images_data['image']))
                image_dict={"image_id":image_id,"image_url":image}
                image_array.append(image_dict)
            
            video_array=[]
            for video_data in upload_video_serializer.data:
                video_id=video_data['id']
                video=urljoin(url,(video_data['video']))
                video_dict={"video_id":video_id,"video_url":video}
                video_array.append(video_dict)
            
            threed_array=[]
            for threed_data in three_d_model_file_serializer.data:
                threed_file_id=threed_data['id']
                threed_file=urljoin(url,(threed_data['File']))
                threed_dict={"threed_id":threed_file_id,"threed_url":threed_file}
                threed_array.append(threed_dict)
            
            response_data = {
                'image_designs':image_array,
                'upload_videos': video_array,
                'three_d_model_files':threed_array
            }

            return Response({"data":response_data},status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'message': 'No detail found with this User.'}, status=status.HTTP_404_NOT_FOUND)



class Get_targetImageByProjectId(APIView):
    def get(self, request,project_id):
            if  Project_Content.objects.filter(project_id=project_id).exists():
                target_image = Project_Content.objects.filter(project_id=project_id).values('target_image')
                target_data=target_image[0]['target_image']
                targeturl=urljoin(background_url,target_data)
            
                return Response({"data":targeturl},status=status.HTTP_200_OK)
            else:
     
                return Response({'message': 'No detail found with this project.'}, status=status.HTTP_404_NOT_FOUND)





# class TestSceneView(APIView):
#     def get(self, request, pk):
#         if not Scene.objects.filter(id=pk).exists():
#             return Response({"message": "Data Not Found"}, status=status.HTTP_400_BAD_REQUEST)

#         scene_array = self.get_scene_data(pk)
#         button_array = self.get_button_data(pk)
#         text_array = self.get_text_data(pk)
#         image_array = self.get_image_data(pk)
#         video_array = self.get_video_data(pk)
#         threed_array = self.get_threed_data(pk)

#         array = [{"id": pk, "scene_data": scene_array, "button_data": button_array, "text_data": text_array,
#                   "image_data": image_array, "video_data": video_array, "ThreeDmodeldata": threed_array}]
#         return Response({"message": "Success", "data": array}, status=status.HTTP_200_OK)

#     def get_scene_data(self, pk):
#         scene_array = []
#         scenes = Scene.objects.filter(id=pk).order_by('id')
#         serializer = SceneSerializer(scenes, many=True)
#         for scene_data in serializer.data:
#             scene_id=scene_data['id']
#             scene_name=scene_data['name']
#             FeaturedtrackerOption=scene_data['FeaturedtrackerOption']
#             if scene_id==pk:
#                 scene_transition=list(Scene_Transition.objects.filter(scene_id=scene_id).values())
#                 scene_photoUI=list(Scene_PhotoUI.objects.filter(scene_id=scene_id).values())
#                 scene_transition_dict = scene_transition[0] if scene_transition else {}
#                 scene_photoUI_dict = scene_photoUI[0] if scene_photoUI else {}
#                 scene_dict_array = [
#                     {
#                     "scene_name":scene_name,
#                     "FeaturedtrackerOption":FeaturedtrackerOption,
#                     "scene_transition": scene_transition_dict,
#                     "scene_photoUI":scene_photoUI_dict ,
#                     }]
#                 scene_array.append(scene_dict_array)
#         return scene_array


#     def get_button_data(self, pk):
#         button_array=[]
#         button=Create_Button.objects.all().order_by('id')
#         serializer_class=ButtonSerializer(button,many=True)
#         for createbuttondata in serializer_class.data:
#             scene_id=createbuttondata['scene_id']
#             if scene_id==pk:
#                 button_id=createbuttondata['id']
#                 button_name=createbuttondata['Button_name']
#                 button_transform=list(Button_Transform.objects.filter(button_Id=button_id).values())
#                 button_transition=list(Button_Transition.objects.filter(button_Id=button_id).values())
#                 button_text=list(Button_Text.objects.filter(button_Id=button_id).values())
#                 button_appearance=list(Button_Appearance.objects.filter(button_Id=button_id).values())
#                 button_action=list(Button_Action.objects.filter(button_Id=button_id).values())
#                 button_transition_dict = button_transition[0] if button_transition else {}
#                 button_transform_dict = button_transform[0] if button_transform else {}
#                 button_text_dict = button_text[0] if button_text else {}
#                 button_appearance_dict = button_appearance[0] if button_appearance else {}
#                 button_action_dict = button_action[0] if button_action else {}
#                 button_dict_array = [
#                     {
#                     "button_id":button_id,
#                     "button_name":button_name,  
#                     "button_transition": button_transition_dict,
#                     "button_transform": button_transform_dict,
#                     "button_text": button_text_dict,
#                     "button_appearance": button_appearance_dict,
#                     "button_action": button_action_dict}]
                
                
#                 button_array.append(button_dict_array)
#         return button_array

#     def get_text_data(self, pk):
#         text=Create_Text.objects.all().order_by('id')
#         serializer_class1=CreateText_Serializer(text,many=True)
#         text_array=[]
#         for create_text_data in serializer_class1.data:
#             scene_id=create_text_data['scene_id']
#             if scene_id==pk:
#                 text_name=create_text_data['Text_name']
#                 text_id=create_text_data['id']
#                 text_transform=list(Text_Transform.objects.filter(text_id=text_id).values())
#                 text_action=list(Text_Action.objects.filter(text_id=text_id).values())
#                 text_transition=list(Text_Transition.objects.filter(text_id=text_id).values())
#                 text_text=list(Text_Text.objects.filter(text_id=text_id).values())
#                 text_transform_dict = text_transform[0] if text_transform else {}
#                 text_action_dict = text_action[0] if text_action else {}
#                 text_transition_dict = text_transition[0] if text_transition else {}
#                 text_text_dict = text_text[0] if text_text else {}
#                 text_dict_array = [
#                     {
#                     "text_id":text_id,
#                     "button_name":text_name,  
#                     "text_transition": text_transition_dict,
#                     "text_transform": text_transform_dict,
#                     "text_text": text_text_dict,
#                     "text_action": text_action_dict}]
#                 text_array.append(text_dict_array)
#         return text_array

#     def get_image_data(self, pk):
#         image=ImageDesign.objects.all().order_by('id')
#         serializer_class2=ImageDesignSerializer(image,many=True)
#         image_array=[]
#         for image_data in serializer_class2.data:
#             scene_id=image_data['scene_id']
#             if scene_id==pk:
#                 image_id=image_data['id']
#                 image_url = urljoin(url,image_data['image'])
#                 image_transform=list(Image_Transform.objects.filter(image_id=image_id).values())
#                 image_appearance=list(Image_Appearance.objects.filter(image_id=image_id).values())
#                 image_action=list(Image_Action.objects.filter(image_id=image_id).values())
#                 image_transition=list(Image_Transition.objects.filter(image_id=image_id).values())
#                 image_transform_dict = image_transform[0] if image_transform else {}
#                 image_appearance_dict = image_appearance[0] if image_appearance else {}
#                 image_action_dict = image_action[0] if image_action else {}
#                 image_transition_dict = image_transition[0] if image_transition else {}
#                 image_dict_array = [
#                     {
#                     "image_id":image_id,
#                     "image_url":image_url,  
#                     "image_transform": image_transform_dict,
#                     "image_appearance": image_appearance_dict,
#                     "image_action": image_action_dict,
#                     "image_transition":image_transition_dict}]
#                 image_array.append(image_dict_array)
#         return image_array

#     def get_video_data(self, pk):
#       pass

#     def get_threed_data(self, pk):
#         pass
