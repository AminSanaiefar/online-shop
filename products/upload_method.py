import os
from uuid import uuid4


def product_image_upload(instance, filename):
    # Get the file extension
    ext = filename.split('.')[-1]
    # Generate a unique filename using uuid4
    unique_filename = f"{uuid4().hex}-{instance.title}.{ext}"
    return os.path.join('products/products_cover', unique_filename)
