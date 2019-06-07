# django2
https://brew.sh/


## 1. iterm2 + zsh
- [iTerm2 + Oh My Zsh 打造舒适终端体验](https://www.jianshu.com/p/9c3439cc3bdb)
- [zsh 下Anaconda的安装](https://www.jianshu.com/p/74b1c60148e8)
  
之前使用mac自带终端sh命令，安装了anaconda3 可以使用python3 和 pip。 但是iterm设置为默认终端后，并该用zsh命令，全部都不可以使用了。

按照上面都说法，将anaconda环境变量导入至```.zshrc```中，即可使conda和pip命令，默认python3
```zsh
david@DaviddeMacBook-Pro  ~  pip --version
pip 18.1 from /Users/david/anaconda3/lib/python3.7/site-packages/pip (python 3.7)
```
## 2. python virtualenv

#### 2.1 virtualenv
```
david@DaviddeMacBook-Pro  ~  pip install virtualenv
```
虚拟环境，就是一个代码运行环境而已，文件系统和物理机mac一样。
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


