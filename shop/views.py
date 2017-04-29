"""
Creates views for shop application
"""

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Shop
from .forms import ShopForm


def shop_create(request):
    """
    create shop
    """
    form = ShopForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        # after creation - redirect to Shop page
        messages.success(request, "Successfully created shop")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Shop was not successfully created!")

    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)


def shop_edit(request, id=None):
    """
    edit shop
    """
    instance = get_object_or_404(Shop, id=id)  # look for given id, if not present - render 404 error

    # param instance - edit an instance (fill the fields)
    form = ShopForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Shop successfully edited", extra_tags="extra_safe")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "name": instance.name,
        "instance": instance,
        "form": form,
    }
    return render(request, "post_form.html", context)


def shop_delete(request, id=None):
    """
    delete shop
    """
    instance = get_object_or_404(Shop, id=id)  # look for given id, if not present - render 404 error

    instance.delete()
    messages.success(request, "Deletion of shop with id {0} completed".format(id))

    return redirect("shop:list")


def shop_detail(request, id=None):
    """
    display shop info
    """
    instance = get_object_or_404(Shop, id=id)  # look for given id, if not present - render 404 error
    context = {
        "name": instance.name,
        "instance": instance,
    }
    return render(request, "shop_detail.html", context)


def shop_list(request):
    """
    list of shops
    """
    queryset = Shop.objects.all()
    context = {
        "name": "List",
        "object_list": queryset
    }
    return render(request, "index.html", context)
