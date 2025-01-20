from django.db import models
from django.contrib.auth.models import AbstractUser

import os
from uuid import uuid4

from products.models import Product


def user_profile_picture_upload(instance, filename):
    # Get the file extension
    ext = filename.split('.')[-1]
    # Generate a unique filename using uuid4
    unique_filename = f"{uuid4().hex}.{ext}"
    # Create a path like 'profile_pics/user_<user_id>/<unique_filename>'
    return os.path.join('profile_picture', f'{instance.email}_{instance.id}', unique_filename)


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to=user_profile_picture_upload, blank=True, null=True)

    def __str__(self):
        return self.email
