# URL命名

因为随着业务变动，网址会变化，而代码也要全部跟着修改路由网址。直接命名一个网址，方便后期变更路由网址

Demo：一个项目中2个app，front（index，login） + CMS（index，login）

# 1. 创建Demo
```
(django-env)  david@MBP  ~/PycharmProjects/first-project  django-admin startproject demo_url
(django-env)  david@MBP  ~/PycharmProjects/first-project  ls
demo_project demo_url     django-env
(django-env)  david@MBP  ~/PycharmProjects/first-project  cd demo_url
(django-env)  david@MBP  ~/PycharmProjects/first-project/demo_url  ls
demo_url  manage.py
(django-env)  david@MBP  ~/PycharmProjects/first-project/demo_url  python manage.py startapp front
(django-env)  david@MBP  ~/PycharmProjects/first-project/demo_url  python manage.py startapp cms
```
```
~/PycharmProjects/first-project/demo_url
├── cms
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── front
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── demo_url
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── settings.cpython-37.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```
# 2. app develop
## 2.1 front
### 1. views
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse('Front index')

def login(request):
    return HttpResponse('Front Login')
```
### 2. create urls.py in current app path
- create urls.py
  ```python
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('', views.index),
      path('login/', views.login)
  ]
  ```
### 3. glocal urls.py
import include 来调用app本地的url路由

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('front.urls')),
    path('cms/', include('cms.urls'))
]
```

## 2.2 cms

### 1. views
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse('CMS index')

def login(request):
    return HttpResponse('CMS Login')
```

### 2. create urls.py in app path
- create urls.py
  ```python
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('', views.index),
      path('login/', views.login)
  ]
### 3. glocal urls.py
all have been done above

# 3. Advanced Functions
##  3.1 If no username passed， redirect to login page
使用GET请求来传递参数的方式进行
```python
from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse('Front index, welcome {} !'.format((username)))
    else:
        return redirect('/login/')
```
## 3.2 If route urls changed
















