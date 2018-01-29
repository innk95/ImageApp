# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Image
from .forms import UploadForm
import urllib.request
import pprint
# Create your views here.

def index(request):
    images = Image.objects.all()
    return render(request, 'index.html', {'images': images})


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            if post.url and not post.file:
                try:
                    img_name = post.url.split('/')[-1]
                    img = urllib.request.urlopen(post.url).read()
                    out = open('media/images/' + img_name, 'wb')
                    out.write(img)
                    out.close()
                    post.url = img_name
                    post.save()
                    return redirect('/')
                except:
                    return redirect('../error/')
            elif not post.url and post.file:
                post.url = request.FILES['file'].name
                print('ok')
                post.save()
                return redirect('/')
            else:
                return redirect('../error/')
        return redirect('../error/')
    else:
        form = UploadForm()
        return render(request, 'upload.html', {'form': form})

def error(request):
    return render(request, 'error.html')

def detail(request, image_id):
    image_list = Image.objects.all()
    image_take = int(image_id)
    context = {'image_list': image_list, 'image_take': image_take}
    return render(request, 'image.html', context)

