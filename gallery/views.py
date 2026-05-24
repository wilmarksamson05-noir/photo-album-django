from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Album

class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'gallery/album_list.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)
    
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Album

class AlbumCreateView(CreateView):
    model = Album
    fields = ['title', 'description']
    template_name = 'gallery/album_form.html'
    success_url = reverse_lazy('album_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
from django.shortcuts import get_object_or_404
from .models import Photo

class PhotoCreateView(CreateView):
    model = Photo
    fields = ['image', 'caption']
    template_name = 'gallery/photo_form.html'

    def form_valid(self, form):
        album = get_object_or_404(Album, pk=self.kwargs['pk'])
        form.instance.album = album
        return super().form_valid(form)

    def get_success_url(self):
        return '/'
    
from django.views.generic import DetailView

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'gallery/album_detail.html'
    context_object_name = 'album'

from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = 'gallery/album_detail.html'
    context_object_name = 'album'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)