# django2
https://brew.sh/


## 1. iterm2 + zsh
- [iTerm2 + Oh My Zsh 打造舒适终端体验](https://www.jianshu.com/p/9c3439cc3bdb)
- [zsh 下Anaconda的安装](https://www.jianshu.com/p/74b1c60148e8)
  
之前使用mac自带终端sh命令，安装了anaconda3 可以使用python3 和 pip。 但是iterm设置为默认终端后，并该用zsh命令，全部都不可以使用了。

按照上面都说法，将anaconda环境变量导入至```.zshrc```中，即可使conda和pip命令，默认python3
- `export PATH="/Users/yong/opt/anaconda3/bin:$PATH"`

```zsh
david@DaviddeMacBook-Pro  ~  pip --version
pip 18.1 from /Users/david/anaconda3/lib/python3.7/site-packages/pip (python 3.7)
```

> **更新 200227**
- 即使使用pip安装，也是由anaconda的python3.7安装，不是安装到系统自带的python2.7中
- 使用pip3安装virtualenv，会安装到系统自带的python3.7环境中
- 如果没有安装anaconda3，那么系统如果只有一个python3环境，使用pip直接安装到python3中
  - 如果存在两个版本的python，那么pip安装到python2中，pip3安装到python3中
```
yong@MacBookPro ~ % pip --version
pip 19.2.3 from /Users/yong/opt/anaconda3/lib/python3.7/site-packages/pip (python 3.7)

yong@MacBookPro ~ % pip3 --version
pip 19.0.3 from /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/site-packages/pip (python 3.7)
```
## 2. python virtualenv

#### 2.1 virtualenv
```
david@DaviddeMacBook-Pro  ~  pip install virtualenv
```
虚拟环境，就是一个代码运行环境而已，**文件系统和物理机mac一样，也有自己的pip工具**
  - 虚拟环境单独创建一个文件目录做管理，所有python虚拟环境全部放到一个目录下
  - 而创建python项目时，需要单独存放到另外一个专门用户代码项目的目录
  - 即，虚拟环境放在：/Users/david/python-envs, 项目放在/Users/david/PycharmProjects
  

创建虚拟环境
- ```cd /Users/david/python-envs```
- ```virtualenv django-env```
- ```. django-env/bin/activate```

创建项目目录
- ``` cd PycharmProjects```
- ```mkdir first-project```

#### 2.2 python -m venv
与上面将 python虚拟环境 和 项目代码 放在不同目录下 不同，下面是将二者放到同一个大目录下

所有虚拟环境，和项目code 全部在创建的同一个文件夹PycharmProjects/django-project下面

```
 david@DaviddeMacBook-Pro  ~/PycharmProjects  mkdir first-project
 david@DaviddeMacBook-Pro  ~/PycharmProjects  cd first-project
 david@DaviddeMacBook-Pro  ~/PycharmProjects/first-project  python -m venv django-env
 david@DaviddeMacBook-Pro  ~/PycharmProjects/first-project  source django-env/bin/activate
(django-env)  david@DaviddeMacBook-Pro  ~/PycharmProjects/first-project  pip install django
(django-env)  david@DaviddeMacBook-Pro  ~/PycharmProjects/first-project  ls
django-env
(django-env)  david@DaviddeMacBook-Pro  ~/PycharmProjects/first-project  django-admin startproject django_project
(django-env)  david@DaviddeMacBook-Pro  ~/PycharmProjects/first-project  ls
django-env     django_project
(django-env)  david@DaviddeMacBook-Pro  ~/PycharmProjects/first-project 
```
## 3. run webserver
#### 3.1 local access
- ```cd django_project```
- ```python manage.py runserver [port9000]```, port default=8000,也可以手动指定

#### 3.2 same subnet access

- edit settings.py
```diff
/Users/david/PycharmProjects/first-project/django_project/django_project/settings.py
- 28 ALLOWED_HOSTS = []
+ 28 ALLOWED_HOSTS = ['192.168.0.4']
```
- ```python manage.py runserver 0.0.0.0:7000```，监听所有ip访问7000端口
- access http://192.168.0.4:7000/ 
<p align="center">
    <img src="https://i.loli.net/2019/06/07/5cf9f8f1c70f232273.jpeg" alt="Sample"  width="200" height="420">
</p>

# 4, start app
    
```
(django-env)  david@MBP  ~/PycharmProjects/first-project/django_project  python manage.py startapp book
(django-env)  david@MBP  ~/PycharmProjects/first-project/django_project  ls
```
```
(django-env)  david@MBP  ~/PycharmProjects/first-project/django_project  tree
.
├── book
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── django_project
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── settings.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── wsgi.cpython-37.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```
# 5. view, URL pass params
每个app的视图函数 view.py中的函数，第一个参数必须是request，绝对不能少，返回值必须是HttpresponseBase子类。

这个request对象中包含来所有客户端传递过来的信息。

## 5.1 URL传递参数1，可传递多个参数
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





## 5.2 URL传递参数2：查询字符串？，GET请求

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
  
  
  
  
  
  
  
  
  
