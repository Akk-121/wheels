from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from main.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/postStatus', StatusApi.as_view()),
    path('api/getPlus', ProductApi.as_view()),
    path('api/StatusOrderApi', StatusOrderApi.as_view()),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
