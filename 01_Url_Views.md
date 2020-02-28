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
2. [常用]使用http get方法，直接将url中问好？后面的键值对传递给视图函数，而视图函数无需提前定义该变量

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

- 前端html中的input控件中的name值和value值 会显示再url中的？后面
- django 的Urls.py分析传递过来的url后将参数分析出来，再在视图函数中通过get方法获得参数
- 控件使用：[30days_frontend:form](https://github.com/davidkorea/30days_frontend/blob/master/form.md)

设置如下

- views
  ```python
  def author_details(request):                        # 无需传递参数变量
    author_id = request.GET.get('id')                 # URL中通过 .../?id=123，GET请求来传递参数
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

# 3. Url的模块化 include()函数详解
如果项目越来越大，所有url都放在全局urls里面管理太乱，因此每个app都将管理所有有关本app的urls路由

项目全局urls.py只负责大类别的路由，具体细节路由由各个app内部urls.py负责
```python
// project urls.py
from django.urls import path,include
urlpatterns = [
    path('', index),
    path('book/', include('book.urls'))
    # 所有book/开头的url都讲使用book.urls里面的规则
]
```
所有book/开头的url都将使用book.urls里面的规则
```python
// book urls.py
from .import views
urlpatterns = [
    path('', views.book),    # 返回hostnaame/book/
    path('details/', views.book_details)  # 返回hostnaame/book/details
]
```



-----

-----

