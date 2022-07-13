from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,response,Http404,HttpResponseRedirect



# Create your views here.

def index(request):
    return render(request,'chat/index.html')
def room1(request):
    return render(request,'chat/room1.html')
def room2(request):
    return render(request,'chat/room2.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })