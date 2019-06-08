# django request and response
# 1. Create a django project and app named apis
- create a django venv, pip install django, source activate
- django-admin startproject wx_test_1 project
- manage.py startapp apis
- create a "views" PythonPackage(__init__.py will be created by default) under apis app path, and create a weather.py view under views PythonPackage
  ```python
  from django.http import HttpResponse

  def helloworld(request):
      method = request.method
      meta = request.META
      cookies = request.COOKIES
      print(method)
      print(meta)
      print(cookies)
      paras = request.GET   # GET方法获得的是一个字典，需要遍历后展示出来
      text = []
      for k, v in paras.items():
          text.append((k,v))
      return HttpResponse(text)
  ```
- create a urls.py under apis app path
  ```python
  from django.urls import path
  from .views import weather

  urlpatterns = [
      path('', weather.helloworld),
  ]
  ```
- global urls.py
  ```python
  from django.urls import path, include
  from django.http import HttpResponse

  def index(request):
      return HttpResponse('Index page')

  urlpatterns = [
      path('', index),
      path('weather/', include('apis.urls'))
  ]
  ```
- global settings.py, comment out csrf middleware
  ```diff
  -   'django.middleware.csrf.CsrfViewMiddleware',
  +   # 'django.middleware.csrf.CsrfViewMiddleware',
  ```
- runserver
  ![](https://i.loli.net/2019/06/08/5cfb448ac786349064.png)
  
# 2. HttpResponse, JsonResponse, FileResponse
```
from django.http import HttpResponse, JsonResponse, FileResponse
```
- weather.py view
  ```python
  from django.http import HttpResponse, JsonResponse, FileResponse

  def helloworld(request):
      method = request.method
      meta = request.META
      cookies = request.COOKIES
      paras = request.GET
      # text = []
      # for k, v in paras.items():
      #     text.append((k,v))
      # return HttpResponse(text)
      return JsonResponse(paras)
  ```
  ```
  from django.http import HttpResponse, JsonResponse, FileResponse

  def helloworld(request):
      data = {
          "method": "GET",
          "meta": "meta",
          "cookies": "cookies"
      }
      return JsonResponse(data=data, safe=False, status=201)
      # safe=False, 不检查是否为JSON格式，可以将python dict只是输出显示
  ```
  
  
