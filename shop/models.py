from django.db import models
from django.utils import timezone


def user_directory_path(instance, filename):
    """
    file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    """
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Shop(models.Model):
    """
    create shop model for ims_site
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, )
    description = models.TextField()
    # logo = models.ImageField(upload_to=user_directory_path)
    # logo = models.ImageField('')
    main_category = models.CharField(max_length=50)
    categories = models.TextField()
    shop_level = models.IntegerField()
    is_in_lottery = models.BooleanField(default=False)
    date_of_creation = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def update_shop(self):
        self.date_of_update = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    create category model for ims_site
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name
