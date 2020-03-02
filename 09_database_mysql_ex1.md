1. start project and app(front)
2. global settings
    - `__init__.py` import pymysql, `pymysql.install_as_MySQLdb()`
    - register app
    - templates, add html files when views function is created
    - static, add css / images when views function is created
    - disable crsf middle
    - urls, `from front import views`
3. Overview

| url | views | method | DB, cursor.execute() |
|-|-|-|-|
| '' | `index()` | **GET** | `select * from book` |
| add_book/ | `add_book()` | **POST**, Form(name, author) | `insert into book(id,name,author) values(null,$name,$author)` |
| book_details/\<int:book_id\>/ | `book_details(book_id)` | **GET** | `select * from book where id=$book_id` |
| book_delete/\<int:book_id\>/ | `book_delete(book_id)` | **GET** | `delete from book where id=$book_id` |
 
4. templates
    - base.html, header nav-bar
    - index.html
    - add_book.html
    - book_detail.html
    - book_delete.html
    
5. 按照功能分门别类设置 视图函数 和 模板tml
    

# 1. 首页

### 1.1 模板
index.html
```html
{% extends 'base.html' %} 
{% block content %}
<div>index page</div>
<div class="bookList">
    {% for item in db %}
    <div class="book">
        <div class="item">
            <!-- 序号不使用item.0，因为数据库中的序号可能不连续  -->
            <div>No. {{ forloop.counter }} </div> 
            <div>Book： {{ item.1 }} </div>
            <div>Author： {{ item.2 }} </div>
        </div>
        <div class="btns">
            <a href="{% url 'book_details' book_id=item.0 %}">
                <!--  标签里面使用变量，直接调用即可，无需在使用花括号，否则报错  -->
                <div class="show">Show</div>
            </a>
            <a href="{% url 'book_delete' book_id=item.0 %}">
                <div id="{{ item.0 }}" class="delete">Delete</div>
            </a>
        </div>
    </div>
    {% endfor %}
</div>
{% endblock %}
```

### 1.2 视图函数

```python
from django.shortcuts import render, redirect, reverse
from django.db import connection

def get_cursor():
    cursor = connection.cursor()
    return cursor

def index(request):
    context = {}
    cursor = get_cursor()
    cursor.execute("select * from book")
    rows = cursor.fetchall()
    context['db'] = rows  
    return render(request, 'index.html', context=context)
```


# 2. 添加数目页面

### 2.1 模板

```html
{% extends 'base.html' %} 
{% block content %}
<div>add book</div>
<div class="addBook">
    <form action="" method="POST" autocomplete="off">
        <!-- action留空，即为提交到当前url下，即add_book.html, -->
        <!-- 通过这个url对应的add_book视图函数来处理 -->
        <table>
            <tbody>
                <tr>
                    <td>Name:</td>
                    <td><input type="text" name="name"></td>
                </tr>
                <tr>
                    <td>Author:</td>
                    <td><input type="text" name="author"></td>
                </tr>
                <tr>
                    <td></td>
                    <td><input type="submit" value="Submit"></td>
                </tr>
            </tbody>
        </table>
    </form>
</div>
{% endblock %}
```
- `<form action="">`，action为空，表示将表单的input键值对`name:value`提交到当前url地址
- `autocomplete="off"`，取消输入框历史记录下拉框


### 2.2 视图函数

```python
def add_book(request):
    if request.method == 'GET':                    // 显示页面
        return render(request, 'add_book.html')
    elif request.method == 'POST':                 // 提交表单数据
        name = request.POST.get('name')
        author = request.POST.get('author')
        cursor = get_cursor()
        cursor.execute("insert into book(id,name,author) values(null,'%s','%s')" % (name, author))
        return redirect(reverse('index'))
```

# 3. 详情界面











# 1. Form

## 1.1 crsf
```html
<form action="" method="POST">
  <input type="text" name="name">
  <input type="submit"m value="Submit">
</form>
```
<img width="677" src="https://user-images.githubusercontent.com/26485327/75646974-5c2c4680-5c86-11ea-80df-64203ac3a65b.png">

```python
// global settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
## 1.2 取消输入框历史记录提示
`autocomplete="off"`

```html
<form action="" method="POST" autocomplete="off>
  <input type="text" name="name">
  <input type="submit"m value="Submit">
</form>
```






