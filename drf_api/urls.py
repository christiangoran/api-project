from django.contrib import admin
from django.urls import path, include
from .views import root_route

urlpatterns = [
    path('', root_route, name='root'),
    path('admin/', admin.site.urls),
    path('admin-auth/', include('rest_framework.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('', include('profiles.urls')),
    path('', include('posts.urls')),
    path('', include('comments.urls')),
    path('', include('likes.urls')),
    path('', include('followers.urls')),
]
