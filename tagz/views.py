from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
import json


from models import *


@login_required
def home(request):
    template_name = 'tagz.html'
    user = get_object_or_404(User, id=request.user.id)
    tagz = user.tagz.all().order_by('text')
    chunks_final = []
    for tag in tagz:
        if tag.chunks is not None:
            for chunk in tag.chunks.all():
                print chunk.text
                chunks_final.append(chunk)
    chunks_final = set(chunks_final)
    return render(request, template_name, {'tagz': tagz, 'chunks': chunks_final})

def get_chunks(request):
    if request.method == "POST":
        tag_id = request.POST.get("tagz")
        if tag_id != "all":
            tagz = get_object_or_404(Tagz, id=tag_id)
            chunks = tagz.chunks.all()
        else:
            user = get_object_or_404(User, id=request.user.id)
            tagz = user.tagz.all()
            chunks=[]
            for tag in tagz:
                if tag.chunks is not None:
                    for chunk in tag.chunks.all():
                        chunks.append(chunk)
            chunks = set(chunks)
        return render(request, 'chunks.html', {'chunks': chunks})

def redirect(request):
    return redirect(home(request))


def logout_view(request):
    logout(request)
    template_name = 'logout.html'
    return render(request, template_name)

@csrf_protect
def new_tag(request):
    if request.method == 'POST':
        user = get_object_or_404(User, id=request.user.id)
        tag = Tagz()
        tag.text = request.POST.get('text')
        tag.save()
        user.tagz.add(tag)
        user.save()
        return JsonResponse({'text': tag.text, 'id': tag.id})

@csrf_protect
def delete_tag(request):
    if request.method == 'POST':
        user = get_object_or_404(User, id=request.user.id)
        tag = get_object_or_404(Tagz, id=request.POST.get("tag_id"))
        user.tagz.remove(tag)
        tag.delete()
        user.save()
        return HttpResponse('deleted')

@csrf_protect
def new_chunk(request):
    if request.method == 'POST':
        tagz = json.loads(request.POST.get("tagz"))
        tags = []
        for item in tagz:
            tags.append(item['id'])

        chunk = Chunks()
        chunk.text = request.POST.get("text")
        chunk.save()
        for tag in tags:
            db_tag = get_object_or_404(Tagz, id=tag)
            db_tag.chunks.add(chunk)
            db_tag.save()

    return JsonResponse({'text':chunk.text})

@csrf_protect
def delete_chunk(request):
    if request.method == 'POST':
        chunk = get_object_or_404(Chunks, id=request.POST.get("chunk_id"))
        chunk.delete()
    return HttpResponse('chunk-again')
