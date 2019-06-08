# apis

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
      text = [method, meta, cookies]

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
  
  
  
  
  
  
  
  
