# django2
https://brew.sh/


# 1. iterm2 + zsh
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
# 2. python virtualenv virtualenvwrapper

## 2.1 virtualenv
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

## 2.2 virtualenvwrapper
上面的virtualenv 需要自己将python虚拟单独放到一个目录，再把项目代码放到其他项目

virtualenvwrapper创建个虚拟环境时，不论在哪个目录下运行，都会将环境创建在固定的文件目录下


## 2.3 python -m venv

> 我觉着，与其安装上面的三方包，还不如自带的好用！！！！
> 与上面将 python虚拟环境 和 项目代码 放在不同目录下 不同，另一种思路是将二者放到同一个大目录下。但是还是推荐分开存放，否则每一个项目都需要创建一个单独的运行环境，太浪费了

- `python -m venv $venv_Name`，是从python3.3版本开始自带的工具，使用和virtualenv类似，但是2.7版本不能使用venv
- 需要先进入到存放虚拟环境的目录，再运行上面的命令，以将新虚拟环境创建在该目录下

所有虚拟环境，和项目code 全部在创建的同一个文件夹PycharmProjects/django-project下面。但是推荐将运行环境和项目分开管理
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
# 3. run webserver
## 3.1 local access
- ```cd django_project```
- ```python manage.py runserver [port9000]```, port default=8000,也可以手动指定

## 3.2 same subnet access

- edit settings.py
```diff
/Users/david/PycharmProjects/first-project/django_project/django_project/settings.py
- 28 ALLOWED_HOSTS = []
+ 28 ALLOWED_HOSTS = ['192.168.0.4']
```
- **[重要步骤]```python manage.py runserver 0.0.0.0:7000```，监听所有ip访问7000端口**，端口可以自行执行，但是`runserver 0.0.0.0`必须要做，否则局域网内ip访问不生效！！！
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

# 5. Debug

settings.py 文件中默认开始Debug模式`DEBUG = True`
1. 保存变更后，启动重启网页服务，实时更新变更内容
2. 网页和console同时提示报错
3. 生产环境要禁止DEBUG，否则对用户不友好，且外人可以看到源码，有安全隐患
    ```python
    DEBUG = False
    ALLOWED_HOSTS = ['13.197.150.200', '127.0.0.1']
    ```
    - debug关闭后，django要求必须指定服务器地址或者域名以用于外部访问，否则程序报错









  
  
  
  
  
  
  
