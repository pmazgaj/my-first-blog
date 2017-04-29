from django.contrib import admin
from .models import Shop
from .models import Category


class ShopModelAdmin(admin.ModelAdmin):
    """
    Model for Shop model in Shop application
    """
    # all
    list_display = ["id", "name", "description",
                    "main_category", "shop_level", "is_in_lottery",
                    "date_of_creation", "date_of_update"]

    # clickable model fields
    list_display_links = ['name']

    # filtering via fields
    list_filter = ["id", "name", "description",
                   "main_category", "shop_level", "is_in_lottery",
                   "date_of_creation", "date_of_update"]

    # editable from main view
    list_editable = ['description']

    # searching via fields
    search_fields = ["name"]

    class Meta:
        model = Shop


class CategoryModelAdmin(admin.ModelAdmin):
    """
    Model for Category model in Shop application
    """
    list_display = ["id", "name", "visible"]

    # clickable model fields
    list_display_links = ['name']

    # filtering via fields
    list_filter = ["id", "name", "visible"]

    # searching via fields
    search_fields = ["name"]

    class Meta:
        model = Category


admin.site.register(Shop, ShopModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
