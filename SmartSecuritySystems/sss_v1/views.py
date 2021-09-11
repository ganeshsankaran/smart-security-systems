from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RawVideoForm, SearchForm, UserForm
from .models import RawVideo, Video
from .utils import get_video_metadata, get_video_thumbnail, get_video_labels

def features(request):
    return render(request, 'features.html', {'user': request.user})

def home(request):
    return render(request, 'home.html')

@login_required
def portal(request):
    return render(request, 'portal.html', {'user': request.user})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login')

        return render(request, 'register.html', {'form': form, 'user': request.user})

    return render(request, 'register.html', {'form': UserForm(), 'user': request.user})

@login_required
def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            label = request.POST.get('label')
            videos = Video.objects.filter(metadata__objects__has_key=label, user=request.user)

            return render(request, 'search.html', {'form': form, 'videos': videos, 'user': request.user})

        return render(request, 'search.html', {'form': form, 'user': request.user})

    return render(request, 'search.html', {'form': SearchForm(), 'user': request.user})

@login_required
def upload(request):
    if request.method == 'POST':
        form = RawVideoForm(request.POST, request.FILES)

        if form.is_valid():
            raw_video = form.save()
            metadata = get_video_metadata(raw_video)
            thumbnail = get_video_thumbnail(raw_video)
            labels = get_video_labels(metadata)

            if request.user.is_authenticated:
                video = Video.objects.create(labels=labels, metadata=metadata, thumbnail=thumbnail, user=request.user)
            else:
                video = Video.objects.create(labels=labels, metadata=metadata, thumbnail=thumbnail)

            RawVideo.objects.filter(pk = raw_video.pk).delete()

            return render(request, 'upload.html', {'video': video, 'user': request.user})
        
        return render(request, 'upload.html', {'form': form, 'user': request.user})
    
    return render(request, 'upload.html', {'form': RawVideoForm(), 'user': request.user})