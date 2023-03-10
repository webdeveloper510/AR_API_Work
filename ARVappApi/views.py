from rest_framework import generics
from .models import Video
from .serializers import VideoSerializer

class VideoList(generics.ListCreateAPIView):
    allowed_methods = ('GET', 'POST')
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    def videoPath(self):
        user = self.request.user
        video = Video.objects.all()
        return video