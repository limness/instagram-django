
from .models import Image, Description

from PIL import Image as ImagePIL


def get_total_image_size() -> float:
    """Get total image size in MB"""
    total_mb = 0
    for object in Image.objects.all():
        total_mb += object.image.file.size / 1024 / 1024

    return round(total_mb, 4)

def get_total_unique_images() -> int:
    """Get unique images by name"""
    total_unique_files = set()
    for object in Image.objects.all():
        image = ImagePIL.open(object.image)
        total_unique_files.add(tuple(image.getdata()))

    return len(total_unique_files)

def get_total_unique_descriptons() -> int:
    """Get unique descriptons by text"""

    total_unique_descriptons = set()
    for object in Description.objects.all():
        total_unique_descriptons.add(object.description)

    return len(total_unique_descriptons)

def form_stat() -> str:
    """Form stats"""
    data = {
        "Total_Images" : Image.objects.count(),
        "Total_Unique_Images" : get_total_unique_images(),
        "Total_Size_Mb" : get_total_image_size(),
        "Total_Descriptons" : Description.objects.count(),
        "Total_Unique_Descriptons" : get_total_unique_descriptons(),
    }
    return data
