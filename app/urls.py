from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("memos.urls")),   # new
    path('admin/', admin.site.urls),
]
