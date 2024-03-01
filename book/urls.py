from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    

    path('details/<int:id>/', views.DetailBookView.as_view(), name='detail_book'),
    path('comment/<int:id>/', views.CommentView.as_view(), name='review'),
    path('details/bye/<int:id>/', views.ByeNow, name='detail_bye'),
]
