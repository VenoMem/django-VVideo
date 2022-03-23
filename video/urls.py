from django.urls import path
from . import views
from .views import VideoCreateView, VideoListView, VideoDetailView, VideoDeleteView, VideoUpdateView

app_name = 'video'

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('video/new/', VideoCreateView.as_view(), name='video-create'),
    path('video/list/', VideoListView.as_view(), name='video-list'),
    path('video/<int:pk>/', VideoDetailView.as_view(), name="video-detail"),
    path('video/<int:pk>/delete/', VideoDeleteView.as_view(), name="video-delete"),
    path('video/<int:pk>/update/', VideoUpdateView.as_view(), name="video-update"),
]
