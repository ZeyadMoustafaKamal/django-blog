from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('post/', include('posts.urls')),
    path('admin/', admin.site.urls),
]
