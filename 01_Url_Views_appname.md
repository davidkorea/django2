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
        return redirect('/login/')          #重定向url，字符串格式的url地址
```
## 3.2 If route urls changed, Nmae a url

if modify url login -> signin, the urls.py and views.py redirect in the local app path should be changed both. For a easy way, give an url a name, and reverse a name to a real url.
- urls.py
    ```python
    from django.urls import path
    from . import views
    urlpatterns = [
        path('', views.index, name='index'),
        path('signin/', views.login, name='login')  # url改名为signin，但是该url的名字为login
    ]
    ```
- views.py
    ```python
    from django.http import HttpResponse
    from django.shortcuts import redirect, reverse
    
    def index(request):
        username = request.GET.get('username')
        if username:
            return HttpResponse('Front index, welcome {} !'.format((username)))
        else:
            return redirect(reverse('login'))       # 现将名字为login路径反转为url，再重定向至该url  
    ```

## 3.3 应用命名空间

因为前端和后台都有index和login两个页面。如果各自的url都取名为name=index和name=login，那么`redirect(reverse('login'))`时，django会一脸懵逼，不能正确路由。使用app_name, `redirect(reverse('app_name:login'))`来重定向。

- front urls.py
    ```python
    from django.urls import path
    from . import views

    app_name = 'front'

    urlpatterns = [
        path('', views.index, name='index'),
        path('signin/', views.login, name='login')
    ]
    ```
- cmd urls.py
    ```python
    from django.urls import path
    from . import views

    app_name = 'cms'

    urlpatterns = [
        path('', views.index, name='index'),
        path('login/', views.login, name='login')
    ]
    ```
- front view redirect
    ```python
    from django.http import HttpResponse
    from django.shortcuts import redirect, reverse
    
    def index(request):
        username = request.GET.get('username')
        if username:
            return HttpResponse('Front index, welcome {} !'.format((username)))
        else:
            return redirect(reverse('front:login'))
    ```








