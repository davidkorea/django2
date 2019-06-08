# Django request and response & RESTful API
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
      paras = request.GET
      return JsonResponse(paras)  # 无需遍历字典，直接输出JSON
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
![](https://i.loli.net/2019/06/08/5cfb479b470f666501.png)
  
# 3. Weather api implement

- third party api
  - signup https://www.juhe.cn/ , get appkey
- create a PythonPackage name thiredparty, create a py file for request weather to juhe api
- create a function in the weather view, when django web get a paras named "city", then call third party api 

## 3.1 juhe api 业务逻辑代码
/Users/david/PycharmProjects/wx_test_1/thirdparty/juhe_api.py
```python
import requests

def weather(city):
    juhe_api = 'http://apis.juhe.cn/simpleWeather/query'
    key = 'xxxxxxxxxxxxxxxxxxx'                           # get in juhe console
    param= '?city={}&key={}'.format(city, key)
    query_url = juhe_api + param                          # full request api
    print(query_url)
    request = requests.get(url=query_url)                 # request GET mothod to juhe api server
    # json_data = json.loads(request.text)
    json_data = request.json()
    result = json_data.get('result')                      # 聚合 返回参数说明，架构会变
    data = {}
    data['city'] = result.get('city')
    data['temperature'] = result.get('realtime').get('temperature')
    data['wind_direction'] = result.get('realtime').get('direct')
    data['wind_strength'] = result.get('realtime').get('power')
    data['humidity'] = result.get('realtime').get('humidity')
    return data

weather('济南')
```
## 3.2 weather view
```python
def weather_app(request):
    if request.method == 'GET':
        city =request.GET.get('city')
        juhe_response = juhe_api.weather(city)
        return JsonResponse(data=juhe_response, status=200)
    elif request.method == 'POST':
        received_body = json.loads(request.body)    # POST的请求内容在body内
        cities = received_body.get('cities')        # cities是一个列表，这个名称是自己定的，postman发送POST请求时用
        response = []                               # 请求是一个list，返回也是list
        for city in cities:
            result = juhe_api.weather(city)
            response.append(result)
        return JsonResponse(data=response, safe=False, status=200)    # safe=False，因为这是list，不是json
```
## 3.3 weather app urls
```python
from django.urls import path
from .views import weather

urlpatterns = [
    path('', weather.weather_app),
]
```
## 3.4 测试GET

http://127.0.0.1:8000/weather/?city=长沙

![](https://i.loli.net/2019/06/08/5cfb642daf57739215.png)

## 3.5 测试POST

![](https://i.loli.net/2019/06/08/5cfb64331814076453.png)


# 4. RESTful API
1. project settings -> `ROOT_URLCONF = 'wx_test_1.urls'`
2. wx_test_1.urls -> `urlpatterns = ['api/v1/', include('api_v1.urls')]`
3. api_v1.urls -> `urlpatterns = ['service/', include('apis.urls')]`
4. apis.urls -> `urlpatterns = ['weather/', weather.weather_app]`

- global urls
  ```diff
  - # path('weather/', include('apis.urls'))
  + path('api/v1', include('wx_test_1.api_v1'))
  ```
- create a py file named "api_v1" under global path, /Users/david/PycharmProjects/wx_test_1/wx_test_1/api_v1.py
  ```python
  from django.urls import path,include

  urlpatterns = [
      path('service/', include('apis.urls'))
  ]
  ```
- apis app urls
  ```python
  from django.urls import path
  from .views import weather

  urlpatterns = [
      # path('', weather.weather_app),
      path('weather/', weather.weather_app),
  ]
  ```
- access api: http://127.0.0.1:8000/api/v1/service/weather/?city=长沙

  ![](https://i.loli.net/2019/06/08/5cfb6a5b56e4a51686.png)




























