# wxapp向django请求图文信息

- 文字信息，请求1次，即可获取所需信息
- 图片信息，请求2次。第一次请求获得资源链接地址，第二期请求根据资源地址获得图片信息

# 1. django后台返回图片信息
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
from utils import response

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

# return  a json which contains image file name and url.
def image_test(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        img_file = os.path.join(settings.IMAGE_PATH, md5 + '.jpg')
        if not os.path.exists(img_file):
            return response.wrap_json_response(
                code=response.ReturnCode.RESOURCE_NOT_EXIST)
        else:
            response_data = {}
            response_data['name'] = md5 + '.jpg'
            response_data['url'] = '/service/image/?md5=%s' % (md5)
            data = response.wrap_json_response(data=response_data)
            return JsonResponse(data=data, safe=False)
```
- 返回图片文件，推荐使用Fileresponse
  - `return HttpResponse(content=data, content_type='image/jpg')`
  - `return FileResponse(open(img_file, 'rb'), content_type='image/jpg')`
## 1.3 url
```python
from .views import weather, menu, image

urlpatterns = [
    path('weather/', weather.weather_app),
    path('menu/', menu.get_menu),
    path('image/', image.image),
    path('imagetext/', image.image_test)
    ]
```
## 1.4 test 
- copy a image file to the resources/images dir named 11111.jpg for test
- access image file: http://127.0.0.1:8000/api/v1/service/image/?md5=11111

    ![](https://i.loli.net/2019/06/09/5cfc93024712416737.png)
- access image text: http://127.0.0.1:8000/api/v1/service/imagetext/?md5=11111
    ![](https://i.loli.net/2019/06/09/5cfc94063fa7285123.png)