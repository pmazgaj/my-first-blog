"""
Creates views for shop application
"""

from django.contrib import messages
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import ShopForm
from .models import Shop


def validate_user(request):
    """
    return True if user is superuser or staff, else raise 404
    """
    if not request.user.is_superuser or not request.user.is_staff:
        raise Http404

    return True


def shop_create(request):
    """
    create shop, with superuser or staff members validation
    """
    validate_user(request)

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
    validate_user(request)

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
    validate_user(request)

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

    context = {
        "name":        "List of shops",
        "object_list": queryset
    }
    return render(request, "shop_list.html", context)
