
# Url命名
1. include模块化
2. url命名
3. app应用命名空间
4. 实例命名空间



# 1. 创建Demo
因为随着业务变动，网址会变化，而代码也要全部跟着修改路由网址。直接命名一个网址，方便后期变更路由网址

Demo：一个项目中2个app
1. 前端 front（index，login） 
2. 后台 CMS（index，login）



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
## 1.1 front
### 1. views
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse('Front index')

def login(request):
    return HttpResponse('Front Login')
```
### 2. create urls.py in current app path
当前app的PythonPackage里面创建一个针对当前app的url.py文件

- create urls.py in front app
  ```python
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('', views.index),
      path('login/', views.login)
  ]
  ```
### 3. global urls.py
import include 来调用app本地的url路由

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('front.urls')),    // 引用app的本地路由文件
    path('cms/', include('cms.urls'))
]
```

## 1.2 cms
因为前台和后台分别有 首页 和 登录 功能，函数从上面完整复制下来即可
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
### 3. global urls.py
path('cms/',inclued('cms/urls'))




# 2. Url命名，页面重定向

实际项目中url的变更很常见，比如登录页面的url需要从login改成signin
- 这种情况下需要对项目全局的urls.py中为每个路由，命名，这样不论子页面的路径名称如何变化，其他页面只调用其名称即可
- 如下 访问主页时，重定向至登录页面

##  2.1 重定向
If no username passed， redirect to login page

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
## 2.2 url命名

> 无论url路径怎么变，只要命名name不变，随时可以引用

if modify url login -> signin, the urls.py and views.py redirect in the local app path should be changed both. For a easy way, give an url a name, and reverse a name to a real url.
- app urls.py
    ```python
    from django.urls import path
    from . import views                             # 当下路径下导入views文件
    urlpatterns = [
        path('', views.index, name='index'),
        path('signin/', views.login, name='login')  # url改名为signin，但是该url的名字为login
    ]
    ```
- app views.py
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

# 3. 应用命名空间

不同app具有相同的url名name，会出现页面路由错误，通过在各自app内的urls.py中为每个app设置一个`app_name`来解决

因为前端和后台都有index和login两个页面。如果各自的url都取名为name=index和name=index，那么`redirect(reverse('login'))`时，django会一脸懵逼，不能正确路由

**在app的urls.py中使用app_name**, `redirect(reverse('app_name:login'))`来重定向。

- front urls.py
    ```python
    from django.urls import path
    from . import views

    app_name = 'front'              // 给每个app去取个名字，用于url定向

    urlpatterns = [
        path('', views.index, name='index'),
        path('signin/', views.login, name='login')
    ]
    ```
- cms urls.py
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

# 4. 实例命名空间
同一个app，分别由两个不同的url对应
- hostname/cms1/ -> cms app
- hostname/cms2/ -> cms app

实例命名空间就是，如上，有几个url的映射，就有几个实例

还是上面的场景，url中传递username参数，则返回cms index页面，否则重定向至cms login页面，出现混乱
- 无username，访问cms1/，重定向至cms1/login
- 无username，访问cms2/，依然，重定向至cms1/login

因此需要对不同实例，在全局urls.py中创建一个唯一的实例命名空间。这样在视图函数中重定向时，可以根据实例命名空间进行重定向


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
    +       current_namespace = request.resolver_match.namespace        # 获取当前url的namespace
    +       return redirect(reverse('%s:login'%current_namespace))
    ```

> **若使用实例命名空间，必须要指定应用命名空间app_name，必须同时指定，否则程序报错**



-----

-----


# 1. include()函数详解

> 上面说到， 如果使用实例命名空间namespace，则必须设定应用命名空间app_name，二者搭配使用。处理分别创建这两个命名空间，还可以在全局urls.py中一并设定

> - **下面两种方式，不如上面的方法常用，因为不够简洁，不好理解。了解下面的2种用法就可以。我不用，但我懂**

## 1.1 全局url中设置app命名空间

也可以，不在app目录下的url指定应用命名空间app_name，直接在global url中指定
```python
urlpatterns = [
    path('cms/', include(('cms.urls', app_name), namespace=None))  # tuple中（子模块url，app_name ）
]
```
```python
urlpatterns = [
    path('cms/', include(('cms.urls', 'cms'), namespace=None))  # tuple中（子模块url，app_name ）
]
```

## 2.2 直接将app目录下的url内容写在include（）函数内
```python
from book import views

path('book/', include([
    path('', views.book),
    path('list/', views.book_list)
])),
```





# 2. re_path() 正则表达式匹配url
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
    - `r""`, raw text, 原生字符串，无需在使用转移字符，用于正则表达式
    - 正则表达式 以`^`开始， `$`结尾
    - `re_path(r"^$", views.article)`, 开始和结尾之前为空，匹配到article函数
    - `re_path(r"^list/$", views.article_list)`，开始和结尾之前只包含‘list/’，匹配article_list
    - `(?P<paras>)`，正则表达式中的变量需要使用圆括号()，如果变量有名字，则需要在括号内部使用问好和大写字母P，`(?P<参数名字>)`，该参数名字也需要在视图函数中指定
    - `(?P<year>\d{4})`，变量year，四位正数，`(?P<month>\d{2})`，变量month，两位整数
    - `r"^list/(?P<year>\d{4})/(?P<month>\d{2})/$"`，匹配list/oooo/oo 的网址，o为整数
    
**除非必须要使用正则表达式使用re_path()，否则path就可以了，否则今天写完正则后，明天看不明白什么意思**

![](https://i.loli.net/2019/06/07/5cfa81a7b1e8649572.png)



# 3. reverse()

对url命名后，使用reverse反转url，需要设置参数时，可以传递`kwargs`参数到reverse()


## 3.1 参数方式传递参数

```python

url = reverse('login', kwargs={"username":"david", "id":1})
```


## 3.2 GET方式获取?参数

需要手动拼接字符串

```python
def login(request, username, id)
  url = reverse('login') + '?username=username&id=id/'
```


# 4. 获取多页数据，首页默认不显示页数

- `hostname/`，虽然url没有显示，确是显示page 1 的数据，
- `hostname/page/2`，从第二页开始，url开始出现页面信息


```python
// urls.py

urlpatterns = [
    path('', views.page),
    path('page/<int:page>/', views.page)
]
```
```python
// views.py

from django.http import HttpResponse

page_list = ['page0', 'page1', 'page2', 'page3']

def page(request, page=0):
    return HttpResponse(page_list[page])
```
- 指定默认参数，用于匹配url规则，否则会报错

![Feb-28-2020 16-38-50](https://user-images.githubusercontent.com/26485327/75524440-da030e80-5a48-11ea-8a84-10c0c330193b.gif)







































