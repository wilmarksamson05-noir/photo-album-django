from django.urls import path
from .views import AlbumListView, AlbumCreateView, PhotoCreateView, AlbumDetailView

urlpatterns = [
    path('', AlbumListView.as_view(), name='album_list'),
    path('create/', AlbumCreateView.as_view(), name='album_create'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
    path('album/<int:pk>/add-photo/', PhotoCreateView.as_view(), name='add_photo'),
]