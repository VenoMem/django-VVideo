from django.urls import path
from . import views
from .views import VideoCreateView, VideoListView, VideoDetailView, VideoDeleteView, VideoUpdateView

app_name = 'video'

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('video/new/', VideoCreateView.as_view(), name='video_create'),
    path('video/list/', VideoListView.as_view(), name='video_list'),
    path('video/<int:pk>/', VideoDetailView.as_view(), name="video_detail"),
    path('video/<int:pk>/delete/', VideoDeleteView.as_view(), name="video_delete"),
    path('video/<int:pk>/update/', VideoUpdateView.as_view(), name="video_update"),
]
