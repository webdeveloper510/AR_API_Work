from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import project3dmodel_detail , project3dmodel_list

urlpatterns = [
    path("video-upload/" , views.VideoList.as_view() ),
    path("create-project/" , views.CreateProjectList.as_view() ),# modify
    path("publish_project/" , views.PublishProject.as_view() ),# new
    path("getpublish_list/<int:user_id>/" , views.GetPublish_Project_list.as_view() ),# new
    path('project-list/<str:pk>/',views.ProjectDetailView.as_view()),
    path('project-label/',views.CreateProjectLabel.as_view()),#new
    path('project_label_list/<int:user_id>/',views.ProjectLabelList.as_view()),#new
    path('project_label_update/<int:pk>/',views.ProjectLabelUpdate.as_view()),#new
    path('signup/', views.UserRegistrationView.as_view()),#modify
    path('resend-verify-email/', views.ResendVerifyEmail.as_view()),#new
    path('verified-email/', views.EmailVerified.as_view()),#new
    path('update-project/<str:pk>/',views.UpdateProjectView.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path('userprofile/', views.ProfileView.as_view()),
    path('editprofilephoto/', views.UpdateCustomerProfilePhoto.as_view()),
    path('changepassword/', views.ChangePasswordView.as_view()),
    path('forget-password/', views.ForgetPasswordView.as_view()),#new
    path('reset-password/', views.ResetPasswordView.as_view()),#new
    path('projects/<int:pk>/', views.ListProjectView.as_view()),
    path('project3dmodel/', project3dmodel_list, name='project3dmodel-list'),
    path('project3dmodel/<int:pk>/', project3dmodel_detail, name='project3dmodel-detail'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('upload-file/', views.UploadFileAPIView.as_view(), name='upload-file'),
    path('GetuploadFile/<int:user_id>/', views.GetUploadFilebyUser_id.as_view(), name='upload-file'),
    

]

# serve static media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
