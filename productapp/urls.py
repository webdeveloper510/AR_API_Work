from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from productapp.views import *

urlpatterns = [
    path('buttons/', ButtonAPIView.as_view()),
    path('buttons/<int:pk>/', ButtonAPIView.as_view(), name='button-detail'),
    path('button_transform/', Button_TransformAPIView.as_view(), name='button_transform'),
    path('button_transform/<int:pk>/', ButtonTransformAPIView.as_view()),
    path('button_transition/', Button_TransitionAPIView.as_view(), name='button_transition'),
    path('button_transition/<int:pk>/', ButtonTransitionAPIView.as_view()),
    path('button_text/', Button_TextAPIView.as_view(), name='button_text'),
    path('button_text/<int:pk>/', ButtonTextAPIView.as_view()),
    path('button_appearance/', Button_AppearanceAPIView.as_view(), name='button_appearance'),
    path('button_appearance/<int:pk>/', ButtonAppearanceAPIView.as_view()),
    path('button_action/', Button_ActionAPIView.as_view(), name='button_action'),
    path('button_action/<int:pk>/', ButtonActionAPIView.as_view()),
    path('GetButtondata/<int:pk>/', GetButtonData.as_view()),
    path('create-text/', Create_TextAPIView.as_view()),
    path('text_transform/', Text_TransformAPIView.as_view(), name='text_transform'),
    path('text_transform/<int:pk>/', TextTransformAPIView.as_view()),
    path('text_transition/', Text_TransitionAPIView.as_view(), name='text_transition'),
    path('text_transition/<int:pk>/', TextTransitionAPIView.as_view()),
    path('text_text/', Text_TextAPIView.as_view(), name='text'),
    path('text_text/<int:pk>/', TextTextAPIView.as_view()),
    path('text_action/', Text_ActionAPIView.as_view(), name='button_action'),
    path('text_action/<int:pk>/', TextActionAPIView.as_view()),
    path('get-all-text-data/<int:pk>/',GetAllTextData.as_view()),
    path('upload-image/', UploadImageView.as_view()),
    # path('upload-image/<int:pk>/', UploadImageView.as_view()),
    path('image_transform/', Image_TransformAPIView.as_view(), name='image_transform'),
    path('image_transform/<int:pk>/', ImageTransformAPIView.as_view(), name='image_transform_update'),
    path('image_transition/', Image_TransitionAPIView.as_view(), name='image_transition'),
    path('image_transition/<int:pk>/', ImageTransitionAPIView.as_view(), name='image_transition_update'),
    path('image_appearance/', Image_AppearanceAPIView.as_view(), name='button_appearance'),
    path('image_appearance/<int:pk>/', ImageAppearanceAPIView.as_view()),
    path('image_action/', Image_ActionAPIView.as_view(), name='Image_action'),
    path('image_action/<int:pk>/', ImageActionAPIView.as_view()),
    path('get-image-data/<int:pk>/',GetImageDataApiView.as_view()),
    path('upload-video/', UploadVideoView.as_view()),
    path('upload-video/<int:pk>/', UploadVideoView.as_view()),
    path('video_transform/', Video_TransformAPIView.as_view(), name='Video_transform'),
    path('video_transform/<int:pk>/', VideoTransformAPIView.as_view(), name='video_transform_update'),
    path('video_transition/', Video_TransitionAPIView.as_view(), name='video_transition'),
    path('video_transition/<int:pk>/', VideoTransitionAPIView.as_view(), name='video_transition'),
    path('video_action/', Video_ActionAPIView.as_view(), name='video_action'),
    path('video_action/<int:pk>/', VideoActionAPIView.as_view()),
    path('get-video-data/<int:pk>/',GetVideoDataApiView.as_view()),
    path('upload-threed-model-file/', ThreeDModelView.as_view()),
    path('upload-threed-model-file/<int:pk>/', UploadVideoView.as_view()),
    path('threed-model_transform/', ThreeDModel_TransformAPIView.as_view()),
    path('threed-model_transform/<int:pk>/', ThreeDModelTransformAPIView.as_view()),
    path('threed-model_transition/', ThreeDModel_TransitionAPIView.as_view()),
    path('threed-model_transition/<int:pk>/', ThreeDModelTransitionAPIView.as_view()),
    path('threed-model_action/', ThreeDModel_ActionAPIView.as_view()),
    path('threed-model_action/<int:pk>/', ThreeDModelActionAPIView.as_view()),
    path('get-threed-model-Data/<int:pk>/',GetThreeDModelDataView.as_view()),

    #---------------------------------------SceneApiView------------------------->

    path('scene/', SceneApiView.as_view()),
    path('scene/<int:pk>/', Scene_APIView.as_view()),
    path('scene_transition/', Scene_TransitionAPIView.as_view()),
    path('scene_transition/<int:pk>/', SceneTransitionAPIView.as_view()),
    path('scene_photoui/', ScenePhotoUI_APIView.as_view()),
    path('scene_photoui/<int:pk>/', ScenePhotoUIAPIView.as_view()),
    path('get-scene-data/<int:pk>/',GetSceneData.as_view()),
    path('scene_details/<int:pk>/',SceneAllDetailById.as_view()),# get all data through scene id
    path('scene_data_by_project/<str:pk>/',GetSceneByProjectId.as_view()), #get all scene through project id
    path('project_content/', ProjectContent_APIView.as_view()),
    path('project_content/<int:pk>/', ProjectContentAPIView.as_view()),
    path('background_sound/', Background_SoundAPIView.as_view()),
    path('background_sound/<int:pk>/', BackgroundSoundAPIView.as_view()),
    path('getproject_contentdata/<int:pk>/', GetProjectContentData.as_view()),
    path('analytics/', Analytics_APIView.as_view()),
    path('analytics/<int:pk>/', AnalyticsAPIView.as_view()),
    path('twod_threed/', TwoD_ThreeD_Switch_APIView.as_view()),
    path('twod_threed/<int:pk>/', TwoD_ThreeDSwitchAPIView.as_view()),
    path('get_projectdata/<int:pk>/', ProjectAllDetailById.as_view()),
    path('user_projects_details/<int:user_id>/', UserDataAPIView.as_view()),
    # path('testview/<int:pk>/', TestSceneView.as_view(), name='test'),
    # recently added api 
    # path('generate_qrcode_for_target_image/', TargetImageQRCodeView.as_view()),
    path('get_targetimage_by_projectid/<str:project_id>/', Get_targetImageByProjectId.as_view()),
    # path('update_publish_key/',Update_Publish_key.as_view()),
    # path('get_publish_data/<int:user_id>/',GetPublishProjectDetail.as_view()),


   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)