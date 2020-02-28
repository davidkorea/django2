# 网址URL与视图View绑定/映射

# 1. Basic
> 200227更新
> - 一个Url对应着一个函数，该函数去执行一些访问数据库等操作
> - 这个函数就叫做视图函数，返回网页视图中所需数据的内容的函数
> - 访问一个网址url就相当于访问一个函数，函数执行的结果展现为网页

```python
// urls.py
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello index')


def book(request):
    return HttpResponse('book page')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),                  // 访问主机名127.0.0.1:8000 返回该页面
    path('book/',book)                // 访问主机名127.0.0.1:8000/book 返回该页面
]
```

- 对于多页面来说，所有url对应的视图函数都写再一起也是不现实的，因此需要将不同页面的视图函数写在其他Python Package里面
    - 在项目根目录下创建 Pycharm - New - Python Package - book
    ```shell
    yong@MacBookPro dj_project_1 % tree -L 2
    .
    ├── book                // 新建Python Package命名为book
    │   ├── __init__.py
    │   ├── __pycache__
    │   └── views.py        // views里面创建book的函数
    ├── db.sqlite3
    ├── dj_project_1
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py         // from book.views import book
    │   └── wsgi.py
    ├── manage.py
    └── venv
        ├── bin
        ├── include
        ├── lib
        └── pyvenv.cfg
    ```
```python
//book/views.py
from django.http import HttpResponse

def book(request):
    return HttpResponse('book page')
```
```python
// urls.py
from book.views import book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('book/', book)
]
```
- 上面手动创建的Python Package在django中叫做app，可以直接通过命令来创建`python manage.py startapp $appName`
  - `(py3-dj2) yong@MacBookPro dj_project_1 % python manage.py startapp movie`

```shell
(py3-dj2) yong@MacBookPro dj_project_1 % tree -L 2                     
.
├── book
│   ├── __init__.py
│   ├── __pycache__
│   └── views.py
├── dj_project_1
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── movie
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   └── views.py
```



# 2. Url传递参数给视图函数
- 每个app的视图函数 view.py中的函数，第一个参数必须是request，绝对不能少，否则报错。返回值必须是HttpresponseBase子类。这个request对象中包含来所有客户端传递过来的信息。
  - HttpresponseBase
    - HttpRequest
    - HttpResponse
    - JSONResponse
    - FileResponse
    - StreamingResponse
    - ...

传递参数有两种方式
1. 再视图函数中写好参数，并在urls.py中的路由设置好对应参数
2. 使用http get方法，直接将url中问好？后面的键值对传递给视图函数，而视图函数无需提前定义该变量

## 2.1 URL传递参数1，可传递多个参数
- ```python manage.py startapp book```， 创建一个app
- book/views.py
  ```
  from django.http import HttpResponse
  
  def book_details(request, book_id, cate_id):    # request必须要有，否则报错，book_id用于路由时传递参数
    text = 'The book id is: {}, the cate id is: {}'.format(book_id, cate_id)
    return HttpResponse(text)                     # 返回必须是一个Httprespose对象或者其子类，否则报错
  ```
- django_project/urls.py
  ```python
  from book import views

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('book/details/<book_id>/<cate_id>', views.book_details)
  ]
  ```
  此时，由于配置了url，所以默认的开启页面消失，如不另行设置，则会报错。所以可以简单写一个，以免看到报错页面
  ```python
  from book import views
  from django.http import HttpResponse

  def index(request):
      return HttpResponse('Index')

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', index),                  # 添加这一行来路由首页面
      path('book/details/<book_id>/<cate_id>', views.book_details), # 此处的<>，为函数中传递的参数变量，不能写错
  ]
  ```
  ![](https://i.loli.net/2019/06/07/5cfa1119bc18078436.png)

- 限制传参的数据类型，字符转换器，如果不满足条件，则无法路由匹配
  ```python
  path('book/details/<book_id>/<int:cate_id>', views.book_details), # 此处的<>，为函数中传递的参数变量，不能写错
  ```
  - str：除了斜杠‘/’以外所有的字符
  - int：一个或多个数字
  - path：所有字符
  - uuid：只有满足`uuid.uuid4()`python自带函数的返回值
    ```python
    >>> import uuid
    >>> uuid.uuid4()
    UUID('1bbb6818-ec33-43aa-b9c1-487edf8b6d3c')
    ```
  - slug：英文中横线，下划线，大小字母，小写字母


## 2.2 URL传递参数2：查询字符串？，GET请求

此方法，视图函数无需写传递参数的变量。使用`request.GET.get('paras in url with ?')`
  
- views
  ```python
  def author_details(request):                        # 无需传递参数变量
    author_id = request.GET.get('id')                 # URL中通过 .../?id=123，G，ET请求来传递参数
    text = 'The author id is : {}'.format(author_id)
    return HttpResponse(text)  
  ```

- urls

  ```python
  ...
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', index),
      path('book/details/<book_id>/<cate_id>', views.book_details),
      path('author/', views.author_details)         # 通过？查询字符串传递参数，不需要<>来匹配
  ]
  ```
- 访问URL：http://127.0.0.1:8000/author/?id=123
  ![](https://i.loli.net/2019/06/07/5cfa180f0aec016071.png)
  
  

-----

-----

-----

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

## 3.4 实例命名空间

当同一个app有2个不同当url时，redirect会乱套，需要给每一个url指定一个名称。比如cms1和cms2两个url都定向于cms app，如果没有username，则重定向到cms/login页面

- global url
    ```python
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('front.urls')),
        path('cms1/', include('cms.urls')),
        path('cms2/', include('cms.urls'))
    ```
- cms view
    ```python
    from django.shortcuts import redirect,reverse

    def index(request):
        username = request.GET.get('username')
        if username:
            return HttpResponse('CMS index')
        else:
            return redirect(reverse('cms:login'))
    ```
    - 当输入 http://127.0.0.1:8000/cms1 时，可以重定向到http://127.0.0.1:8000/cms1/login/ 但是输入http://127.0.0.1:8000/cms2 也重定向到来http://127.0.0.1:8000/cms1/login/ 
    - 因此需要准确路由，需要实例命名

- global url
    ```diff
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('front.urls')),
    -   path('cms1/', include('cms.urls')),
    -   path('cms2/', include('cms.urls'))
    +   path('cms1/', include('cms.urls', namespace='cms1')),
    +   path('cms2/', include('cms.urls', namespace='cms2'))
    ```
- cms view
    ```diff
    from django.shortcuts import redirect,reverse

    def index(request):
        username = request.GET.get('username')
        if username:
            return HttpResponse('CMS index')
        else:
    -       return redirect(reverse('cms:login'))
    +       current_namespace = request.resolver_match.namespace        # 获取当前的namespace
    +       return redirect(reverse('%s:login'%current_namespace))
    ```

> **若使用实例命名空间，必须要指定应用命名空间app_name**

## 3.5 include()函数详解

虽然这样用的不多，但是能看懂别人代码为什么这么些

### 3.5.1 应用命名空间
也可以，不在app目录下的url指定应用命名空间app_name，直接在global url中指定
```python
urlpatterns = [
    path('cms/', include(('cms.urls', 'cms'), namespace=None))  # tuple中（子木块url，app_name ）
]
```
### 3.5.2 直接将app目录下的url内容写在include（）函数内
```python
from book import views

path('book/', include([
    path('', views.book),
    path('list/', views.book_list)
])),
```
# 4. re_path 正则表达式匹配url
**特殊情况再用re_path，能用path就用path**

- 创建一个新的app
    ```sh
    (django-env)  david@MBP  ~/PycharmProjects/first-project/demo_url  python manage.py startapp article
    ```
- global url
    ```diff
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('front.urls')),
        path('cms1/', include('cms.urls', namespace='cms1')),
        path('cms2/', include('cms.urls', namespace='cms2')),
    +   path('article/', include('article.urls'))
    ```

- app article views
    ```python
    from django.http import HttpResponse

    def article(request):
        return HttpResponse('article index')

    def article_list(request):
        return HttpResponse('article list page')

    def article_year_month(request, year, month):
        text = 'The year is: {}, the month is: {}'.format(year, month)
        return HttpResponse(text)
    ```
- app article urls
    ```python
    from django.urls import re_path
    from . import views
    
    urlpatterns = [
        re_path(r"^$", views.article),
        re_path(r"^list/$", views.article_list),
        re_path(r"^list/(?P<year>\d{4})/(?P<month>\d{2})/$", views.article_year_month)
    ]
    ```
    - `r""`, raw text, 用户正则表达式
    - `^`开始， `$`结尾
    - `re_path(r"^$", views.article)`, 开始和结尾之前为空，匹配到article函数
    - `re_path(r"^list/$", views.article_list)`，开始和结尾之前只包含‘list/’，匹配article_list
    - `(?P<paras>)`，用于正则表达式中的变量
    - `(?P<year>\d{4})`，变量year，四位正数，`(?P<month>\d{2})`，变量montj，两位整数
    - `r"^list/(?P<year>\d{4})/(?P<month>\d{2})/$"`，匹配list/oooo/oo 的网址，o为整数

![](https://i.loli.net/2019/06/07/5cfa81a7b1e8649572.png)
















