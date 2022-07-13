from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,response,Http404,HttpResponseRedirect
from .form import FormControlProfile
from .models import Profile
from django.db.models import F


# Create your views here.

def index(request):
    return render(request,'app1/index.html')


def create_Form(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = FormControlProfile(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "app1/create_Form.html",context)


def read(request):

    context={}

    context["dataset"]=Profile.objects.all()

    return render(request,"app1/read.html", context)


def update(request,id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    obj=get_object_or_404(Profile,id=id)

    # add the dictionary during initialization
    form = FormControlProfile(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

        # add form dictionary to context
    context["form"] = form

    return render(request, "app1/update.html", context)

def incrementationOfProduct (request,id):
    context = {}

    # add the dictionary during initialization
    context["data"] = Profile.objects.get(id=id)

    Profile.objects.get(id=id).update(number=F('number') + 1)


    return HttpResponseRedirect("/" + id)

def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id=id)

    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


def detail(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = Profile.objects.get(id=id)

    return render(request, "app1/detail.html", context)


def delete(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Profile, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "app1/delate.html", context)










