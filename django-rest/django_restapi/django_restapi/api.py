from rest_framework import routers
from music import api_views as music_views

routers = routers.DefaultRouter()
routers.register(r'albums', music_views.AlbumViewSet)
routers.register(r'songs', music_views.SongViewSet)
