#  Object Relational Mapping （ORM）

- 采用原生sql，会在代码中出现大量的sql语句，且不可以复用
- 当数据库的一个字段改名后，那么代码中的几乎每一条原生sql语句都要改
- sql注入隐患

ORM 可以通过类的方式去操作数据库，因此**无需手动在数据库中创建表**，而是通过类来创建
- 表 -> 类
- 行 -> 实例
- 列 -> 属性


# 1. 使用ORM创建一个数据库

#### 1. 创建app，并添加值全局设置INSTALLED_APP中
#### 2. 在创建的app中会自动生成models.py文件，用于创建ORM类
#### 3. 将一个普通的python类变成一个可以映射数据到数据库的模型，需要继承django的models.Model父类
```python
from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=200, null=False)
    price = models.FloatField(null=False, default=0)  # default 默认值为0
    
    def __str__(self):
    return "<Book: (id:{id}, name:{name}, author:{author}, price:{price})>".format(
        id=self.id, name=self.name, author=self.author, price=self.price)
```
- `def __str__(self):`**是python类自带的语法，当打印该类时，会按照这个方法的设置进行输入显示**
- 其实id这一行可以不用手动定义，django默认会生成一个id字段并且为自增长的主键
```python
class Publiosher(models.Model):
    name = models.CharField(max_length=100, null=False)
    address =  models.CharField(max_length=100, null=False)
```
<img width="700" src="https://user-images.githubusercontent.com/26485327/76154935-cbd78100-611f-11ea-97cc-fa1cc98f9fe7.png">



#### 4. `python manage.py makemigrations` 生成迁移脚本文件
#### 5. `python manage.py migrate` 将迁移脚本文件映射到数据库
```shell
(dj3) yong@MacBookPro project8_orm % python manage.py makemigrations
Migrations for 'book':
  book/migrations/0001_initial.py
    - Create model Book
    
(dj3) yong@MacBookPro project8_orm % python manage.py migrate       
Operations to perform:
  Apply all migrations: admin, auth, book, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
  Applying book.0001_initial... OK
  Applying sessions.0001_initial... OK
```
- 由于django在INSTALLED_APPS中内置安装的一些app，首次执行migrate时会一并运行这些app的model，一起映射到数据库
<img width="693"  src="https://user-images.githubusercontent.com/26485327/76154858-62a33e00-611e-11ea-90fa-4a507f13551e.png">


- 查看mysql数据库，已经创建好了表，表的名称为book_book，如果不指定表的名字，默认为**app的名_类的名**
<img width="957"  src="https://user-images.githubusercontent.com/26485327/76154878-a72ed980-611e-11ea-8ed2-8203c85446f8.png">


# 2. ORM 增删改查

-



## 2.1 增
```python
# global urls.py
from book import views

urlpatterns = [
    path('', views.index, name='index')
]
```

```python
# book/views.py
from django.http import HTTPResponse
from .models import Book

def index(request):
    book = Book(name='react.js', author='david', price=129)
    book.save()
    return HTTPResponse('Add book ok!')
```
<img width="300" src="https://user-images.githubusercontent.com/26485327/76155081-1e19a180-6122-11ea-8042-567f73a971e3.png">

## 2.2 查
### 2.2.1 根据主键查找
```python
# book/models.py
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=200, null=False)
    price = models.FloatField(null=False, default=0)  # default 默认值为0

    def __str__(self):
        return "<Book: (id:{id}, name:{name}, author:{author}, price:{price})>".format(
            id=self.id, name=self.name, author=self.author, price=self.price)
```
```python
# book/views.py
def index():
    book = Book.objects.get(pk=1)
    print(book)
```
```
<Book: (id:1, name:react.js, author:david, price:129.0)>
```
- `objects`是默认的方法，之后也可以自定义方法
- `pk`是primary key的意思

### 2.2.2 根据其他条件查找
```python
# book/views.py

def index(request):
    books = Book.objects.filter(author='david')
    print(books)
```
```
<QuerySet [<Book: <Book: (id:1, name:react.js, author:david, price:129.0)>>, 
            <Book: <Book: (id:2, name:django web, author:david, price:88.0)>>]>
```
- `objects.filter(key='value')`返回一个数组，即使只有一个满足查询 条件也是数组



## 2.3 删

1. 查
2. 删

```python
book = Book.objects.get(pk=1)
book.delete()
```


## 2.4 改

1. 查
2. 赋新值
3. 保存

```python
book = Book.objects.get(pk=2)
book.price = 55
book.save()
```



















