from rest_framework import viewsets
from .models import Post, Image, File
from .serializers import PostSerializer, ImageSerializer, FileSerializer

# Search
from rest_framework.filters import SearchFilter

# File upload, Parsers
from rest_framework.parsers import MultiPartParser, FormParser

# response 클라이언트가 요청한 형태로 콘텐츠를 렌더링 해준다.
from rest_framework.response import Response

# status HTTP에서 제공하는 상태코드는 숫자로 되어있지만 REST프레임 워크에서는 문자 형태의 식별자를 제공하여 상태를 좀더 잘 구분할 수 있도록 해준다.
from rest_framework import status

# pagination
from .pagination import Mypagination

# authentication 이용자 권한
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

# Permission 호출 권한
# from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

 
class PostViewset(viewsets.ModelViewSet):
	# Viewset 별로 각각인증 적용
	# authentication_classes = [BasicAuthentication, SessionAuthentication]
	# permissions_classes = [IsAuthenticated]
	queryset = Post.objects.all().order_by('id')
	serializer_class = PostSerializer
	pagination_class = Mypagination

	filter_backends = [SearchFilter]
	search_fields = ('title','body')

	# author 자동 지정, 저장
	def perform_crate(self, serializer):
		serializer.save(author = self.request.user)

	# 현재 유저 반화 
		# 현재 request를 보낸 유저 : self,request.user
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

	# parser 다양한 종류의 media type 허용
	parser_classes = (MultiPartParser, FormParser)
	
	def post(self, request, *args, **kwargs):
		serializer = FileSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		else:
			return Response(serializer.error, status=HTTP_400_BAD_REQUEST)


