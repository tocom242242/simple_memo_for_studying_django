from django.urls import path

from . import views

urlpatterns = [
    # /memos/
    path("", views.index, name="index"), 

    # /memos/
    path("insert", views.insert, name="insert_memo"), 

    # /memos/1/
    path("<int:memo_id>/", views.detail, name="detail")
]
