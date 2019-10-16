from django.contrib import admin
from django.urls import path, include
from storage import urls
# 로그인을 위해서
from rest_framework import urls
# media static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('storage.urls')),
	# api 로그인
	path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)