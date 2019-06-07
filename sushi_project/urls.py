from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('restaurants/', include('restaurants.urls')),
    path('user/', include('accounts.urls')),
]
