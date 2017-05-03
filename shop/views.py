"""
Creates views for shop application
"""

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import Http404
from .models import Shop
from .forms import ShopForm


def shop_create(request):
    """
    create shop, with superuser or staff members validation
    """
    if not request.user.is_superuser or not request.user.is_staff:
        raise Http404

    form = ShopForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        # after creation - redirect to Shop page
        messages.success(request, "Successfully created shop with id {}".format(instance.id))
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
    }
    return render(request, "shop_form.html", context)


def shop_edit(request, id=None):
    """
    edit shop, with superuser validation
    """
    if not request.user.is_superuser:
        raise Http404

    instance = get_object_or_404(Shop, id=id)  # look for given id, if not present - render 404 error

    # param instance - edit an instance (fill the fields)
    form = ShopForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Shop successfully edited", extra_tags="extra_safe")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "name":     instance.name,
        "instance": instance,
        "form":     form,
    }
    return render(request, "shop_form.html", context)


def shop_delete(request, id=None):
    """
    delete shop, with superuser validation
    """
    if not request.user.is_superuser:
        raise Http404

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
        "name":     instance.name,
        "instance": instance,
    }
    return render(request, "shop_detail.html", context)


def shop_list(request):
    """
    list of shops
    """
    queryset = Shop.objects.all()
    print(queryset)
    context = {
        "name":        "List of shops",
        "object_list": queryset
    }
    return render(request, "shop_list.html", context)
