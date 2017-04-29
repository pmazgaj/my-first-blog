"""
Creates views for shop application
"""

from django.shortcuts import render
from django.http import HttpResponse
from .models import Shop


def shop_create(request):
    """create shop"""
    return HttpResponse("<h1>Create</h1>")


def shop_edit(request):
    """edit shop"""
    return HttpResponse("<h1>Edit</h1>")


def shop_delete(request):
    """delete shop"""
    return HttpResponse("<h1>Delete</h1>")


def shop_detail(request):
    """display shop info"""
    context = {"title": "Detail"}
    return render(request, "index.html", context)


def shop_list(request):
    """list of shops"""
    queryset = Shop.objects.all()
    context = {
        "title": "List",
        "object_list": queryset
    }
    return render(request, "index.html", context)
