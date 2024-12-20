from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

from products.models import Product


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    rate = models.PositiveIntegerField(default=5,
                                       validators=[MaxValueValidator(5, message="rating can't be more than Five!"),
                                                   MinValueValidator(0, message="rating can't be less than Zero!")])
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}: {" ".join(self.text.split(' ')[:25])}...'
