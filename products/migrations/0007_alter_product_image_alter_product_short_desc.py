# Generated by Django 5.1.4 on 2025-01-01 11:00

import products.upload_method
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_short_desc_alter_product_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=products.upload_method.product_image_upload, verbose_name='Product Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_desc',
            field=models.CharField(max_length=500, verbose_name='Short Description'),
        ),
    ]
