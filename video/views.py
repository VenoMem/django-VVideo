from asyncio import mixins
from pyexpat import model
from aiohttp import request
from attr import fields
from django.shortcuts import render
from .models import Video
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def homepage(request):
    return render(request, "video/homepage.html", {"title": "Homepage"})


class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    fields = ['title','video','description']
    success_url = '/video/list/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.video = self.request.FILES['video']
        return super().form_valid(form)



class VideoListView(LoginRequiredMixin, ListView):
    model = Video
    context_object_name = "videos"
    ordering = ['-date_posted']


class VideoDetailView(LoginRequiredMixin, DetailView):
    model = Video


class VideoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    success_url = "/video/list/"

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.author:
            return True
        return False


class VideoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Video
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        #form.instance.video = self.request.FILES['video']
        return super().form_valid(form)

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.author:
            return True
        return False