

# database

1. install mysql
2. install navicat
3. set mysql db in django
4. install mysqlclient and pymysql, modify django source code -  [django2/3 mysqlclient pymysql "Error loading MySQLdb module. Did you install mysqlclient?" #5](https://github.com/davidkorea/django2/issues/5#issue-573657976)

5. 

# 1. 设置mysql作为数据库

- global settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',         # 数据库引擎
        'NAME': 'django_db1',                         # 数据库名
        'USER': 'root',
        'PASSWORD': '11111111',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}
```

在navicat中，创建数据库和表book
<img width="950" src="https://user-images.githubusercontent.com/26485327/75625148-50913f00-5bf6-11ea-8d3f-ff1d45679840.png">


# 2. 视图函数中操作数据库
- 插入数据
```python
from django.shortcuts import render
from django.db import connection

def index(request):
    cursor = connection.cursor()
    cursor.execute("insert into book(id,name,author) values(null,'david','haha')")
    return render(request, 'index.html')
```
- 以上connect和cursor都是套路写法
- 访问首页后，会执行上面的插入语句
- 查看数据库，该语句插入数据成功
<img width="680" src="https://user-images.githubusercontent.com/26485327/75639053-e2865f80-5c69-11ea-985a-e30bd67bd9e1.png">


- 读取数据
```python
from django.shortcuts import render
from django.db import connection

def index(request):
    cursor = connection.cursor()
    cursor.execute("select * fron book")
    rows = cursor.fetchall()
    for row in rows:
        peint(row)
    return render(request, 'index.html')
```



