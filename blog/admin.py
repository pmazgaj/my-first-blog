"""
Admin panel for each application separately
"""

from django.contrib import admin

# import Post model
from .models import Post

# register model
admin.site.register(Post)

