# Generated by Django 5.1.4 on 2025-01-01 10:15

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
