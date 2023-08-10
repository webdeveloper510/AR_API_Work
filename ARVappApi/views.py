
from ARVisualApi.ar_package import *

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        # 'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def verify_email(email, access_token):
    subject, from_email, to = 'Verify your email', settings.EMAIL_HOST_USER, email
    text_content = 'This is an important message.'
    context = {'verify_url': Verify_url + '/' + access_token}
    html_content = render_to_string('email_verify.html', context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def forget_password_mail(email, access_token):
    subject, from_email, to = 'Forget Password Link', settings.EMAIL_HOST_USER, email
    text_content = 'This is an important message.'
    context = {'Forget_password_url': Forget_password_url + '/' + access_token}
    html_content = render_to_string('forget_password.html', context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

class UserRegistrationView(views.APIView):
    permission_classes = (AllowAny,)
    def post(self,request,format=None):
            firstname=request.data.get('firstname') 
            lastname=request.data.get('lastname') 
            email=request.data.get('email') 
            password=request.data.get('password') 
            image=request.data.get('image') 
            dateofbirth=request.data.get('dateofbirth') 
            proffession=request.data.get('proffession') 
            serializer=UserRegister(data=request.data)
            if User.objects.filter(email=email,Is_verified=False).exists():
                user=User.objects.filter(email=email).first()
                User.objects.update(firstname=firstname,lastname=lastname,
                                    image=image,dateofbirth=dateofbirth,proffession=proffession)
                user.set_password(password)
                user.save()
                token=get_tokens_for_user(user)
                access_token = token['access']
                verify_email(email,access_token)
                return Response({'status':status.HTTP_201_CREATED,'msg':'Email Verification link sent to your email','token':access_token})
            else:    
                
                if serializer.is_valid(raise_exception=True):
                    user=serializer.save()
                    email=email
                    if user is not None:
                        token=get_tokens_for_user(user)
                        access_token = token['access']
                        verify_email(email,access_token)
                    return Response({'status':status.HTTP_201_CREATED,'msg':'Email Verification link sent to your email','token':access_token})
            return Response({errors:serializer.errors},status=status.HTTP_400_BAD_REQUEST)
       
class ResendVerifyEmail(views.APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def post(self, request, format=None):

        try:
            serializer = UserProfileSerializer(request.user)
            email=serializer.data['email']
            user = User.objects.filter(email=email).first()
            token = get_tokens_for_user(user) 
            access_token = token['access']
            verify_email(email, access_token)
            return Response({'status': status.HTTP_200_OK, 'msg': 'Email Verification link sent to your email','token':access_token})

        except Exception as e:
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e)})

class EmailVerified(views.APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        try:
                serializer = UserProfileSerializer(request.user)
                User.objects.filter(email=serializer.data['email']).update(Is_verified=True)
                data_dict={
                    "id":serializer.data['id'],
                    "email":serializer.data['email'],
                    "firstname":serializer.data['firstname'],
                    "lastname":serializer.data['lastname'],
                    "profile_image":urljoin(url,serializer.data['image'])if serializer.data['image'] else None,
                    "dateofbirth":serializer.data['dateofbirth'],
                    "proffession":serializer.data['proffession']
                    }
                return Response({'status':status.HTTP_200_OK,'message':'Email verified successfully','data':data_dict})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})


class UserLoginView(views.APIView):

    def post(self, request):
            username = request.data.get('email')
            password = request.data.get('password')
            user = authenticate(request, username=username, password=password)
            try:
                if not username :
                    return Response({'detail': 'username is required.'}, status=status.HTTP_401_UNAUTHORIZED)
                
                if not password :
                    return Response({'detail': 'password is required.'}, status=status.HTTP_401_UNAUTHORIZED)

                if not user:
                    return Response({'detail': 'Username and password did not match.'}, status=status.HTTP_401_UNAUTHORIZED)
                
                if not User.objects.filter(email=username,Is_verified=True).exists():
                    return Response({'detail': 'Unauthorized user.'}, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    login(request, user)
                    token = get_tokens_for_user(user)
                    userobj ={'id': user.id, 'email': user.email, 'dateofBirth': user.dateofbirth}
                    return Response({'detail': 'Logged in successfully.', 'token': token, 'data': userobj})
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})
                 

class ProfileView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        try:
            serializer = UserProfileSerializer(request.user)
            data_dict={"id":serializer.data['id'],"email":serializer.data['email'],"firstname":serializer.data['firstname'],
                    "lastname":serializer.data['lastname'],"profile_image":urljoin(url,serializer.data['image']),"dateofbirth":serializer.data['dateofbirth'],
                    "proffession":serializer.data['proffession']}
            return Response(data_dict,status=status.HTTP_200_OK)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})

    
class ForgetPasswordView(APIView):
    renderer_classes=[UserRenderer]
    def post(self, request):
        email = request.data.get("email")
        try:
            if not email:
                return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "Email is required"})

            user = User.objects.filter(email=email).first()
            if not user:
                return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "User with this email does not exist"})
            else:
                token = get_tokens_for_user(user) 
                access_token = token['access']
                forget_password_mail(email, access_token)
                return Response({'status': status.HTTP_200_OK, 'msg': 'Forget password Link sent to your email ','token':access_token})
            
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})

class ResetPasswordView(APIView):
    renderer_classes=[UserRenderer]  
    permission_classes=[IsAuthenticated]
    def post(self, request):
        new_password = request.data.get("new_password")
        confirm_password= request.data.get("confirm_password")
        try:
            serializer = UserProfileSerializer(request.user)
            user = User.objects.filter(email=serializer.data['email']).first()
            if not user:
                return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "User with this email does not exist"})
            
            if not new_password:
                return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "New password is required"})
            
            if not confirm_password:
                return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "confirm  password is required"})
            
            if new_password!=confirm_password:
                 return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "new password and confirm  password does not match"},status=status.HTTP_400_BAD_REQUEST)
            else:
               
                user.set_password(new_password)
                user.save()
            
                return Response({'status': status.HTTP_200_OK, 'message': ' Reset password successfully '})

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})

class ChangePasswordView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]

    def post(self, request):
        try:
            serializer = ChangePasswordSerializer(data=request.data)
            if serializer.is_valid():
                # check if the old password is correct
                if not request.user.check_password(serializer.data.get('old_password')):
                    return Response({'old_password': ['Wrong password.']},
                                    status=status.HTTP_400_BAD_REQUEST)

                # set the new password
                request.user.set_password(serializer.data.get('new_password'))
                request.user.save()
                return Response({'message': 'Password updated successfully.'},
                                status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})


class UpdateCustomerProfilePhoto(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        try:
            serializer = UserRegister(request.user,context={"request": request})
            profile_photo = request.data.get('profile_photo')

            if profile_photo:
                user = User.objects.get(id=serializer.data['id'])
                user.image = profile_photo
                user.save()

            return Response({"message": "Your profile photo updated successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})

class UserLogoutView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            logout(request)
            return Response({"status": status.HTTP_200_OK,'detail': 'Logged out successfully.'})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})
   

# USER VIDEO UPLOAD FOR 3D MODEL

class VideoList(generics.ListCreateAPIView):
    allowed_methods = ( 'POST')
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    def videoPath(self):
        user = self.request.user
        video = Video.objects.all()
        return video
    

        
class CreateProjectList(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=CreateProject_Serializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                project=serializer.save()
                
                data_dict={"id":serializer.data['id'],"projectType":serializer.data['projectType'],"triggerType":serializer.data['projectType'],
                        "imagePro":urljoin(url,serializer.data['imagePro']),"ProTitle":serializer.data['ProTitle'],"projectIcon":urljoin(url,serializer.data['projectIcon']),
                        "projectTitle":serializer.data['projectTitle'],"created_at":serializer.data['created_at'],"publish_key":serializer.data['publish_key'],
                        "projectUser":serializer.data['projectUser']}
            
                project_url = "{}/{}/".format(Project_Id_Url,str(serializer.data['id']))
                projectid_or_code = qrcode.make(project_url)
                qr_code_path = f"static/media/projectid_image_qrcode/{serializer.data['id']}.png"
                projectid_or_code.save(qr_code_path)
                qr_code_url= "{}/{}/".format(url,qr_code_path)
                Project_ID=CreateProject.objects.get(id=serializer.data['id'])
                qr_data =Project_ID_QR_Code.objects.create(project_id=Project_ID,project_id_qr_code_url=project_url,qr_code_url=qr_code_url)
                return Response({'message':'Project Created successfully','data':data_dict, 'qr_code_url': qr_code_url},status=status.HTTP_201_CREATED)
        
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})    
          
            
class PublishProject(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        project_id = request.data.get('project_id')
        publish_key = request.data.get('publish_key')
        
        try:
            if not project_id:
                return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "project_id required"})

            if not CreateProject.objects.filter(id=project_id).exists():
                return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "project does not exist"})

            if not publish_key:
                return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "publish_key required"})

            last_inserted_data = Project_ID_QR_Code.objects.filter(project_id=project_id).latest('id')
            if publish_key=='True':
                
                
                if not last_inserted_data.publish_key and last_inserted_data.description is None:
                   
                    last_inserted_data.id
                    description = 'v1'
                    project_url = f"{Project_Id_Url}/{project_id}/{description}"

                    projectid_or_code = qrcode.make(project_url)
                    qr_code_path = f"static/media/projectid_image_qrcode/{project_id}.png"
                    projectid_or_code.save(qr_code_path)
                    qr_code_url = f"{url}/{qr_code_path}"

                    ProjectID = CreateProject.objects.get(id=project_id)
                    update_data= Project_ID_QR_Code.objects.filter(id=last_inserted_data.id,project_id=project_id).update(publish_key=publish_key,project_id_qr_code_url=project_url, qr_code_url=qr_code_url,description=description)
                    Update_Publish_key=CreateProject.objects.filter(id=project_id).update(publish_key=publish_key)
                    return Response({"status": status.HTTP_200_OK,"message": "Project Publish successfully","qr_code_url":qr_code_url})

                elif last_inserted_data.publish_key and last_inserted_data.description is not None:
                  
                    last_description = last_inserted_data.description
                    last_description_number = int(last_description[1:])
                    new_description_number = last_description_number + 1
                    description = f"v{new_description_number}"

                    project_url = f"{Project_Id_Url}/{project_id}/{description}"
                    projectid_or_code = qrcode.make(project_url)
                    qr_code_path = f"static/media/projectid_image_qrcode/{project_id}.png"
                    projectid_or_code.save(qr_code_path)
                    qr_code_url = f"{url}/{qr_code_path}"

                    ProjectID = CreateProject.objects.get(id=project_id)
                    publish_data = Project_ID_QR_Code.objects.create(
                        project_id=ProjectID, publish_key=publish_key, description=description,
                        project_id_qr_code_url=project_url, qr_code_url=qr_code_url
                    )
                    return Response({"status": status.HTTP_200_OK, "message":"Project Publish successfully","qr_code_url":qr_code_url})
                
            if publish_key!='True':
               
                update_publish_key=Project_ID_QR_Code.objects.filter(project_id=project_id).update(publish_key=publish_key)
                Update_Publish_key=CreateProject.objects.filter(id=project_id).update(publish_key=publish_key)
                return Response({"status": status.HTTP_200_OK, "message":"Project Publish updated successfully","publish_key":publish_key})


        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})


 
#Publish List
class GetPublish_Project_list(APIView):
    renderer_classes = [UserRenderer]

    def get(self, request,user_id ,format=None):
        try:
            if not user_id:
                return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "User is required"})

            if not User.objects.filter(id=user_id).exists():
                return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "User does not exist"})

            User_data = User.objects.filter(id=user_id).first()

            project_ids = CreateProject.objects.filter(projectUser=user_id, publish_key=True).values_list('id', flat=True)
            array=[]
            for project_id in project_ids:
                data=Project_ID_QR_Code.objects.all().order_by('id')
                serializer=Project_ID_QR_Code_Serializer(data,many=True)
                
                for x in serializer.data:
                    if project_id==x['project_id']:

                        dict_data={"description":x['description'],"updated_at":x['updated_at']}
                        array.append(dict_data)

            response_data = {
                "user_id": user_id,
                "email": User_data.email,
                "username": User_data.firstname + " " + User_data.lastname,
                "profile_image": urljoin(url, str(User_data.image.url)) if User_data.image else None,
                "project_details": array
                    
            }

            return Response({"status": status.HTTP_200_OK, "message": "success", "data": response_data})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})



# PROJECTS DETAILS BY PROJECT ID

class ProjectDetailView(APIView):
    def get_object(self, pk):
        try:
            return CreateProject.objects.get(pk=pk)
        except CreateProject.DoesNotExist:
             raise Http404


    def get(self, request, pk, format=None):
        try:
            product = self.get_object(pk)
            serializer = CreateProjectSerializer(product)
            qrcode_data=Project_ID_QR_Code.objects.filter(project_id=serializer.data['id']).values('qr_code_url')
            
            response_data = {
                "id": str(serializer.data['id']),
                "imagePro": urljoin(url, serializer.data['imagePro']) if serializer.data['imagePro'] else None,
                "ProTitle": serializer.data['ProTitle'],
                "projectIcon": urljoin(url, serializer.data['projectIcon']) if serializer.data['projectIcon'] else None,
                "projectTitle": serializer.data['projectTitle'],
                "projectUser": serializer.data['projectUser'],
                "created_at": serializer.data['created_at'],
                "projectType": serializer.data['projectType'],
                "triggerType": serializer.data['triggerType'],
                'publish_key': serializer.data['publish_key'],
                'qr_code_url':qrcode_data[0]['qr_code_url']  ,
                "project_label":list(ProjectLabel.objects.filter(projectId=pk,required=True).values('id','project_label','required'))
            }
           
            return Response({"status":status.HTTP_200_OK,"project_details":response_data})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})


    def put(self, request, pk):
        try:
            user = CreateProject.objects.get(pk=pk)
            serializer = CreateProjectSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})

    def delete(self, request, pk, format=None):
        try:
            project = self.get_object(pk)
            project.delete()
            return Response({"message":"project deleted successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})


# LIST OF PROJECTS BY USER_ID

class ListProjectView(APIView):
    
    def get(self, request, pk, format=None):
        try:
            project = CreateProject.objects.all().order_by('id')
            serializer = CreateProjectSerializer(project, many=True)
            response=[]
            for project_data in serializer.data:
              if pk==project_data['projectUser']:

                project_data_dict = {
                "id": (project_data['id']),
                "imagePro": urljoin(url, project_data['imagePro']) if project_data['imagePro'] else None,
                "ProTitle": project_data['ProTitle'],
                "projectIcon": urljoin(url, project_data['projectIcon']) if project_data['projectIcon'] else None,
                "projectTitle": project_data['projectTitle'],
                "projectUser": project_data['projectUser'],
                "created_at": project_data['created_at'],
                "projectType": project_data['projectType'],
                "triggerType": project_data['triggerType'],
                'publish_key': project_data['publish_key'],
                "project_label":list(ProjectLabel.objects.filter(projectId=project_data['id'],required=True).values('id','project_label','required'))
            }
                response.append(project_data_dict)
            
            return Response({"status":status.HTTP_200_OK,"projectlist":response})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})


class UpdateProjectView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request,pk, format=None):
        try:
            imagePro = request.data.get('imagePro')
            ProTitle = request.data.get('ProTitle')
            projectIcon = request.data.get('projectIcon')
            projectTitle = request.data.get('projectTitle')
            triggerType=request.data.get('triggerType')
            publish_key=request.data.get('publish_key')
            if CreateProject.objects.filter(id=pk).exists():
                if not imagePro:
                    imagedata=None
                    
                else:
                    project = CreateProject.objects.get(id=pk)
                    project.imagePro = imagePro
                    project.save()
                    imagedata=urljoin(image_url,str(project.imagePro))
        
                 
                if ProTitle:
                    data=CreateProject.objects.filter(id=pk).update(ProTitle=ProTitle)

                if projectIcon:
                    project = CreateProject.objects.get(id=pk)
                    project.projectIcon = projectIcon
                    project.save()
                    project_icondata=urljoin(image_url,str(project.projectIcon))
                else:
                    project_icondata=None
                
                if projectTitle:
                    data=CreateProject.objects.filter(id=pk).update(projectTitle=projectTitle)
                
                if triggerType:
                    data=CreateProject.objects.filter(id=pk).update(triggerType=triggerType)
                
                if publish_key:
                    data=CreateProject.objects.filter(id=pk).update(publish_key=publish_key)
                dict_data={"imagepro":imagedata,"ProTitle":ProTitle,"projectIcon":project_icondata,"projectTitle":projectTitle,"triggerType":triggerType,"publish_key":publish_key}
                return Response({"message": "Your projects details updated successfully","data":dict_data}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Not Found"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})



# class SaveGLTFModel(APIView):
class SaveGLTFModel(viewsets.ModelViewSet):
    queryset = Project3DModel.objects.all()
    serializer_class = SaveProjectSerializer
    
    def create(self, request):
        # code to handle the creation of a new Project3DModel instance
        pass
    
    def update(self, request, pk=None):
        # code to handle updating an existing Project3DModel instance
        pass
    
    def destroy(self, request, pk=None):
        #  code to handle deleting an existing Project3DModel instance
        pass

project3dmodel_list = SaveGLTFModel.as_view({
    'get': 'list',
    'post': 'create'
})

project3dmodel_detail = SaveGLTFModel.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



class CreateProjectLabel(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        
        try:
            project_id = request.data.get('project_id')
            project_label = request.data.get('project_label')
            user_id = request.data.get('user_id')
            required = request.data.get('required')
            if ProjectLabel.objects.filter(projectId=project_id, project_label=project_label,user_id=user_id).exists():
                if not user_id:
                    return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "user_id is required"})
                
                if not User.objects.filter(id=user_id).exists():
                    return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "user does not exist"})
                
                if not project_id:
                    return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "project_id is required"})
                
                if not CreateProject.objects.filter(id=project_id).exists():
                    return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "project does not exist"})
                
                label_data = ProjectLabel.objects.filter(projectId=project_id, project_label=project_label).update(project_label=project_label, required=required)
                updated_label = ProjectLabel.objects.get(projectId=project_id, project_label=project_label)
                data={"id": updated_label.id,"label_name":project_label}
                return Response({"status": status.HTTP_200_OK, "message": "Label updated successfully", "data": data})
            
            else:
                if not user_id:
                    return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "user_id is required"})
                
                if not User.objects.filter(id=user_id).exists():
                    return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "user does not exist"})
                
                if not project_id:
                    return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "project_id is required"})
                
                if not CreateProject.objects.filter(id=project_id).exists():
                    return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "project does not exist"})
                
                if not project_label:
                    return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "Label is required"})
                
                else:
                    ProjectID = CreateProject.objects.get(id=project_id)
                    UserID = User.objects.get(id=user_id)
                    label_data = ProjectLabel.objects.create(projectId=ProjectID, project_label=project_label, user_id=UserID, required=required)
                    label_data.save()
                    label_id = label_data.id
                    label_name = label_data.project_label
                    Data = {"id": label_id, "label_name": label_name}
                    return Response({"status": status.HTTP_201_CREATED, "message": "Label created successfully", "data": Data})
        
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})


class ProjectLabelList(APIView):
    renderer_classes = [UserRenderer]

    def get(self, request, user_id, format=None):
        try:
            if not ProjectLabel.objects.filter(user_id=user_id).exists():
                return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "User with label does not exist"})
            else:
                product = ProjectLabel.objects.filter(user_id=user_id).order_by('id')
                serializer = ProjectLabel_Serializer(product, many=True)
                label_data = []
                seen_project_labels = set()  # To keep track of seen project_labels

                for project_label_data in serializer.data:
                    project_label = project_label_data['project_label']
                    if project_label not in seen_project_labels:
                        seen_project_labels.add(project_label)
                        label_dict = {
                            "id": project_label_data['id'],
                            "project_label": project_label,
                            "required": project_label_data['required'],
                            "projectId": project_label_data['projectId']
                        }
                        label_data.append(label_dict)

                return JsonResponse({"status": status.HTTP_200_OK, "message": "success", "user_id": user_id, "data": label_data})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})




class ProjectLabelDelete(APIView):
    renderer_classes = [UserRenderer]
        
    def get_object(self, pk):
            try:
                return ProjectLabel.objects.get(pk=pk)
            except ProjectLabel.DoesNotExist:
                raise Http404
   
    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        if product.delete():
            return Response({'message':status.HTTP_200_OK,'success':'True'})
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class UploadFileAPIView(APIView):
    def post(self, request):
        user_id=request.data.get('user_id')
        file=request.data.get('file')
        if not user_id:
                return JsonResponse({"status": status.HTTP_400_BAD_REQUEST, "message": "user_id is required"})
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({"status": status.HTTP_400_BAD_REQUEST, "message": "user does not exist"})
        
        if not file:
            return JsonResponse({"status": status.HTTP_400_BAD_REQUEST, "message": "file field is required"})
        try:
            serializer = UploadFile_Serializer(data=request.data)
            if serializer.is_valid():
                file = serializer.save()
                data={
                    "id":serializer.data['id'],
                    "user_id":user_id,
                    "file":urljoin(url,serializer.data['file'])
                }
                return Response({"status":status.HTTP_200_OK,'message':'file uploaded successfully','data':data})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})


class GetUploadFilebyUser_id(APIView):

    def get(self, request, user_id,format=None):
        try:
            if not  UploadFile.objects.filter(user_id=user_id).exists():
                return Response({"status":status.HTTP_400_BAD_REQUEST,"message":" user with label does not exist"})
            else:
                file = UploadFile.objects.all().order_by('id')
                serializer = UploadFile_Serializer(file, many=True)
                response=[]
                for file_data in serializer.data:
                   if user_id==file_data['user_id']:
                       
                       dict_response={
                           "id":file_data['id'],
                           "file":urljoin(url,(file_data['file']))
                       }
                       response.append(dict_response)
                return Response({'status':status.HTTP_200_OK,'message':'success','data':response})

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": str(e) + " in line " + str(exc_tb.tb_lineno)})