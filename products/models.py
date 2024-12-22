from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.id])


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Comment Author')
    text = models.TextField(verbose_name='Comment Text')
    rate = models.PositiveIntegerField(default=5,
                                       validators=[MaxValueValidator(5, message="rating can't be more than Five!"),
                                                   MinValueValidator(0, message="rating can't be less than Zero!")],
                                       verbose_name='Rate')
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name='Active')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    # Manager
    object = models.Manager()
    active_comments = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.product.id])

    def __str__(self):
        return f'{self.user}: {" ".join(self.text.split(' ')[:25])}...'
