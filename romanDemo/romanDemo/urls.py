from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('romans/', include('demoApp.urls')),
    path('admin/', admin.site.urls),
]