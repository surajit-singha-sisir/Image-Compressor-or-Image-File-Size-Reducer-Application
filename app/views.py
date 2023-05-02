from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse

from PIL import Image


def index(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
        compression_percent = int(request.POST.get('compression_percent', 60))
        image = Image.open(image_file)
        format = image.format
        width, height = image.size
        new_size = (int(width * compression_percent / 100), int(height * compression_percent / 100))
        image = image.resize(new_size)
        compressed_image_file = default_storage.open(image_file.name, 'wb')
        image.save(compressed_image_file, format=format)
        compressed_image_file.close()
        response = HttpResponse(content_type='image/png')
        response['Content-Disposition'] = f'attachment; filename="{image_file.name.split(".")[0]}_compressed.png"'
        compressed_image_file = default_storage.open(image_file.name, 'rb')
        response.write(compressed_image_file.read())
        compressed_image_file.close()
        return response
    else:
        return render(request, 'index.html')
