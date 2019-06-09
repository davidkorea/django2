# wxapp向django请求图文信息

- 文字信息，请求1次，即可获取所需信息
- 图片信息，请求2次。第一次请求获得资源链接地址，第二期请求根据资源地址获得图片信息

# 1. django后台返货图片信息
- create a PythonPackage named as resources/images to restore images, 2 levels are all PythonPackage. the __init__.py can be deleted.
- create a view to deal with images data

## 1.1 global settings add resource path
```python
RESOURCE_PATH = os.path.join(BASE_DIR, 'resources')
IMAGE_PATH = os.path.join(RESOURCE_PATH, 'images')
```
## 1.2 image view
- create a view named as image.py in apis app.
```python
from django.http import HttpResponse, JsonResponse, Http404, FileResponse
from wx_test_1 import settings
import os

# return a piece of image
def image(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        img_file = os.path.join(settings.IMAGE_PATH, md5 + '.jpg')
        if not os.path.exists(img_file):
            return Http404()
        else:
            data = open(img_file, 'rb').read()
            # return HttpResponse(content=data, content_type='image/jpg')
            return FileResponse(open(img_file, 'rb'), content_type='image/jpg')
```
- 返回图片文件，推荐使用Fileresponse
  - `return HttpResponse(content=data, content_type='image/jpg')`
  - `return FileResponse(open(img_file, 'rb'), content_type='image/jpg')`
