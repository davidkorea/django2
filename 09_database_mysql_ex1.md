1. start project and app(front)
2. global settings
    - `__init__.py` import pymysql, `pymysql.install_as_MySQLdb()`
    - register app
    - templates, add html files when views function is created
    - static, add css / images when views function is created
    - disable crsf middle
    - urls, `from front import views`
    - DATABASE mysql
3. Database mysql
    - create table 'book' and add fields to table
    
4. Overview

| url | views | method | DB, cursor.execute() |
|-|-|-|-|
| '' | `index()` | **GET** | `select * from book` |
| add_book/ | `add_book()` | **POST**, Form(name, author) | `insert into book(id,name,author) values(null,$name,$author)` |
| book_details/\<int:book_id\>/ | `book_details(book_id)` | **GET** | `select * from book where id=$book_id` |
| book_delete/\<int:book_id\>/ | `book_delete(book_id)` | **GET** | `delete from book where id=$book_id` |
 
5. templates
    - base.html, header nav-bar
    - index.html
    - add_book.html
    - book_detail.html
    - book_delete.html
    
    
按照功能分门别类设置 视图函数 和 模板html
    

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
- `<form action="">`，action为空，表示将表单的input键值对`name:value`提交到当前网址
- 表单中的input type=submit，自动将表带内部的input内容提交到action中的网址
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

# 3. 详情页面


### 3.1 模板
- index.html
    -  `<a href="{% url 'book_details' book_id=item.0 %}">`，超链接中将当先数目的数据库序号item.0传递给视图函数
```html
{% for item in db %}
 <div class="btns">
    <a href="{% url 'book_details' book_id=item.0 %}">
        <!--  标签里面使用变量，直接调用即可，无需在使用花括号，否则报错  -->
        <div class="show">Show</div>
    </a>
    <a href="{% url 'book_delete' book_id=item.0 %}">
        <div id="{{ item.0 }}" class="delete">Delete</div>
    </a>
</div>
{% endfor %}
```

- book_details.html
```html
{% extends 'base.html' %} {% block content %}
<div>
    book details
    <div style="margin-top:10px">
            <div>name: {{book.1}}</div>
            <div>name: {{book.2}}</div>
    </div>
</div>
{% endblock %}
```


### 3.2 视图函数

```python
def book_details(request, book_id):
    cursor = get_cursor()
    cursor.execute("select * from book where id='%s'" %book_id)
    book = cursor.fetchone()
    return render(request, 'book_details.html',context={'book':book})
```
通过首页按钮的<a>标签，搭配`{% url 'book_detail' book_id=item.0 %}`，将当前数目在数据库中的序号传回来，以用来在数据库中通过`where id=book_id`来检索数据

# 4. 删除数目

### 4.1 模板
由于不需要显示页面，因此无该功能对应的html子页面。但是在主页index.html需要配置。


### 4.2 视图函数

#### 1. <a>标签，搭配`{% url 'book_delete' book_id=item.0 %}`
点击后直接删除，返回首页
    
- index.html
```html
{% for item in db %}
 <div class="btns">
    <a href="{% url 'book_delete' book_id=item.0 %}">
        <div id="{{ item.0 }}" class="delete">Delete</div>
    </a>
</div>
{% endfor %}
```

```python
def book_delete(request, book_id):
    cursor = get_cursor()
    cursor.execute("delete from book where id='%s'" % book_id)
    return redirect(reverse('index'))
```

![Mar-02-2020 15-52-02](https://user-images.githubusercontent.com/26485327/75655900-cbf9fb80-5c9d-11ea-8bc3-8612a8c5f0cf.gif)


#### 2. jQuery AJAX
点击后，先弹出确认删除提示框，同意后删除数据，在弹出删除成功提示框.

- index.html
    - <a>标签的href留空，按钮的点击事件交给js操作
    - 给删除按钮添加id，该id即为该数目在数据库中的索引序号，以用于方便获取该元素
    
```html
{% for item in db %}
 <div class="btns">
    <a href="">
        <div id="{{ item.0 }}" class="delete">Delete</div>
    </a>
</div>

<script>
    $(function() {
        $('#{{ item.0 }}').click(function() {
            var deleteFlag = confirm('Delete {{ item.1 }} ?')
            if (deleteFlag) {
                $.ajax({
                    url: "{% url 'book_delete' book_id=item.0 %}",
                    success: function(resp) {
                        alert(resp)
                    }
                })
            }
        })
    })
</script>
{% endfor %}
```

```python
def book_delete(request, book_id):
    cursor = get_cursor()
    cursor.execute("delete from book where id='%s'" % book_id)
    return HttpResponse('Deleted No. %s ok.' % book_id)
```

![Mar-02-2020 16-00-00](https://user-images.githubusercontent.com/26485327/75656447-ebddef00-5c9e-11ea-8190-0d671ec9acc2.gif)



-----



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






