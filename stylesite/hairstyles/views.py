from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from hairstyles.models import Style, Image
from datetime import datetime, timedelta, tzinfo

def index(request):
    latest_hairstyle_list = Style.objects.order_by('pub_date')[:]
    context = {'latest_hairstyle_list': latest_hairstyle_list}
    return render(request, 'hairstyles/index.html', context)

def detail(request, hairstyle_id):
    try:
        hairstyle = Style.objects.get(pk=hairstyle_id)
    except Style.DoesNotExist:
        raise Http404
    return render(request, 'hairstyles/detail.html', {'hairstyle': hairstyle})

def zoom(request, hairstyle_id):
    try:
        hairstyle = Style.objects.get(pk=hairstyle_id)
    except Style.DoesNotExist:
        raise Http404
    return render(request, 'hairstyles/zoom.html', {'hairstyle': hairstyle})
 
#CRUD Functionality
def add_style(request):
    return render(request, 'hairstyles/add_style.html')
    
def submit_hairstyle(request):
    new_hairstyle = Style.objects.create(name=request.GET.get("hairstyle"), pub_date=datetime.today(), time_of_day=request.GET.get("time"), length=request.GET.get("length"), texture=request.GET.get("texture"), type=request.GET.get("type"))
    new_hairstyle.save()
    s = Style.objects.get(name__startswith=request.GET.get("hairstyle"))
    s.image_set.create(image=request.GET.get("image"))
    latest_hairstyle_list = Style.objects.order_by('pub_date')[:]
    context = {'latest_hairstyle_list': latest_hairstyle_list}
    return render(request, 'hairstyles/index.html', context)
    
# Update function IP    
def update(request, hairstyle_id):
    print "update"
    hairstyle = Style.objects.get(pk=hairstyle_id)
    return render(request, 'hairstyles/detail.html', {'hairstyle': hairstyle})
    
def delete(request, hairstyle_id):
    hairstyle = Style.objects.get(pk=hairstyle_id)
    hairstyle.delete()
    
    latest_hairstyle_list = Style.objects.order_by('pub_date')[:]
    context = {'latest_hairstyle_list': latest_hairstyle_list}
    return render(request, 'hairstyles/index.html', context)
    
#Search Functionality
def search(request):
    return render(request, 'hairstyles/search.html')
    
def search_hairstyle(request):
    time_of_day=request.GET.get("time")
    length=request.GET.get("length")
    texture=request.GET.get("texture")
    type=request.GET.get("type")
    full_list = Style.objects.all()
    id = []
    for a in full_list:
        if length == a.length and texture == a.texture and type == a.type and time_of_day == a.time_of_day:
            id.append(a.id)
    if id != []:
        hairstyle = Style.objects.get(pk=id[0])
        return render(request, 'hairstyles/detail.html', {'hairstyle': hairstyle})
    else:
        return render(request, 'hairstyles/sorry.html')
    
def last_search(request):
    time_of_day, length, texture, type, id = request.GET.get("time"), request.GET.get("length"), request.GET.get("texture"), request.GET.get("type"), request.GET.get("id")
    full_list, ids = Style.objects.all(), []
    for a in full_list:
        if length == a.length and texture == a.texture and type == a.type and time_of_day == a.time_of_day:
            ids.append(a.id)
    place = ids.index(int(id))
    if len(ids) != 1 and place > 0:
        hairstyle = Style.objects.get(pk=ids[place-1])
        return render(request, 'hairstyles/detail.html', {'hairstyle': hairstyle})
    else:
        return render(request, 'hairstyles/search.html')
    
def next_search(request):
    time_of_day, length, texture, type, id = request.GET.get("time"), request.GET.get("length"), request.GET.get("texture"), request.GET.get("type"), request.GET.get("id")
    full_list, ids = Style.objects.all(), []
    for a in full_list:
        if length == a.length and texture == a.texture and type == a.type and time_of_day == a.time_of_day:
            ids.append(a.id)
    place = ids.index(int(id))
    if len(ids) != 1 and place < len(ids)-1:
        hairstyle = Style.objects.get(pk=ids[place+1])
        return render(request, 'hairstyles/detail.html', {'hairstyle': hairstyle})
    else:
        return render(request, 'hairstyles/search.html')
        
def handling_csv(request):
    return render(request, 'hairstyles/upload_csv.html')

def upload_csv(request):
    import csv
    reader = csv.reader(open(request.GET.get("filename","rb")))
    read = []
    for row in reader:
        read.append(row)
    for item in read[1:]:
        new_hairstyle = Style.objects.create(name=item[0], pub_date=datetime.today(), time_of_day=item[1], length=item[2], texture=item[3], type=item[4])
        new_hairstyle.save()
        s = Style.objects.get(name__startswith=item[0])
        s.image_set.create(image=item[5])
    return render(request, 'hairstyles/upload_csv.html')

def clear_all(request):
    for style in Style.objects.all():
        style.delete()
    return render(request, 'hairstyles/upload_csv.html')
