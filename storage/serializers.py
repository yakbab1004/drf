from .models import Post, Image, File
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):

	user = serializers.ReadOnlyField(source='author.username')

	class Meta:
		model = Post
		fields = ('id', 'title', 'body', 'user')


class ImageSerializer(serializers.ModelSerializer):

	user = serializers.ReadOnlyField(source='author.username')
	image = serializers.ImageField(use_url=True)

	class Meta:
		model = Image
		fields = ('id', 'user', 'image', 'desc')

class FileSerializer(serializers.ModelSerializer):

	user = serializers.ReadOnlyField(source='author.username')
	files = serializers.FileField(use_url=True)

	class Meta:
		model = File
		fields = ('id', 'user', 'files', 'desc')