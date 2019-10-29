from rest_framework import viewsets
from .models import Post, Image, File
from .serializers import PostSerializer, ImageSerializer, FileSerializer

# Search
from rest_framework.filters import SearchFilter

# File upload, Parsers
from rest_framework.parsers import MultiPartParser, FormParser

# response
from rest_framework.response import Response
from rest_framework import status

# pagination
from .pagination import Mypagination

# authentication 
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

# Permission 
# from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser


class PostViewset(viewsets.ModelViewSet):
	# Viewset
	# authentication_classes = [BasicAuthentication, SessionAuthentication]
	# permissions_classes = [IsAuthenticated]
	queryset = Post.objects.all().order_by('id')
	serializer_class = PostSerializer
	pagination_class = Mypagination

	filter_backends = [SearchFilter]
	search_fields = ('title','body')

	# author
	def perform_crate(self, serializer):
		serializer.save(author = self.request.user)

	
	def get_queryset(self):
		qs =super().get_queryset()

		if self.request.user.is_authenticated:
			qs = qs.filter(author = self.request.user)
		else:
			qs = qs.none()
		return qs



# image
class ImageViewset(viewsets.ModelViewSet):
	queryset = Image.objects.all().order_by('id')
	serializer_class = ImageSerializer

# file
class FileViewset(viewsets.ModelViewSet):
	queryset = File.objects.all().order_by('id')
	serializer_class = FileSerializer

	# parser 
	parser_classes = (MultiPartParser, FormParser)
	
	def post(self, request, *args, **kwargs):
		serializer = FileSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		else:
			return Response(serializer.error, status=HTTP_400_BAD_REQUEST)


