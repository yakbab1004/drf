from rest_framework.routers import DefaultRouter
from django.urls import path, include
from storage import views

router = DefaultRouter()
router.register('post', views.PostViewset)
router.register('image', views.ImageViewset)
router.register('file', views.FileViewset)

urlpatterns = [
	path('', include(router.urls))
]