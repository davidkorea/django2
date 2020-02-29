
# 模板变量
1. if
2. for
3. with
4. url




# 1. {% with %}{% endwith %}
定义的变量只能在with语块里面使用

```
context = {
  "persons":['david','davidson'],
}
```
```python
<div>
    {% with da=persons.0 %}   // 等号两边不能有空格
        <p>{{ da }}</p>
    {% endwith %}
</div>
```
或
```python
<div>
    {% with persons.0 as da %}  
        <p>{{ da }}</p>
    {% endwith %}
</div>
```

# 2. {% url %}
模板中使用`{% url 'urlName' %}`，来调用urls.py中命名的url路由


```python
// urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('book/', views.book, name="book"),
    path('movie/', views.movie, name="movie")
]
```

```python
// views.py

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def book(request):
    return HttpResponse('book page')

def movie(request):
    return  HttpResponse('movie page')
```

```html
// templates/index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .nav {
            user-select: none;
        }
        
        .nav>ul {
            display: flex;
        }
        
        ul>li {
            list-style: none;
            margin: 5px;
            padding: 5px 20px;
            border: 2px solid gray;
            box-shadow: 0 0 5px black;
        }
        
        a {
            text-decoration: none;
        }
        
        a:visited {
            color: black;
        }
    </style>
</head>

<body>
    <div class="nav">
        <ul>
            <li><a href="{% url 'index' %}">index</a></li>
            <li><a href="{% url 'book' %}">book</a></li>
            <li><a href="{% url 'movie' %}">movie</a></li>
        </ul>
    </div>
</body>
</html>
```
- `<a href="{% url 'index' %}">index</a>`
- `{% url 'index' %}`，urlname 不是用用括号

![Feb-29-2020 12-22-29](https://user-images.githubusercontent.com/26485327/75600743-31a78580-5aee-11ea-9bf8-3852b9934cba.gif)


## 2.1 url传递参数
### 1. 声明变量
{% url 'urlName' id='1' %}

```python
// urls.py
urlpatterns = [
    path('', views.index, name="index"),
    path('book/', views.book, name="book"),
    path('book/<book_id>', views.book_details, name="book_details"),]
```
```python
// views.py
def book_details(request, book_id):
    text = 'the book id is: %s' %book_id
    return HttpResponse(text)
```
```html
// templates/index.html

<li><a href="{% url 'book_details' book_id=1 %}">book List</a></li>
```
- url名后面，空格，直接写参数名和参数值`book_id=1`

### 2. GET？获取变量
```python
// urls.py
urlpatterns = [
    path('login/', views.login, name='login')
]
```

```python
//views.py
def login(request):
    next = request.GET.get('next')      // 通过GET获取？参数
    text = 'the next page is %s' %next
    return HttpResponse(text)
```
```html
// template/index.html
<li><a href="{% url 'login' %}?next=/ ">login</a></li>
```
- GET请求的参数，需要拼接字符串，不能直接按照上面的写法直接写到{% url %}里面

![Feb-29-2020 13-59-56](https://user-images.githubusercontent.com/26485327/75601979-d11f4500-5afb-11ea-8bf8-59c3dcfc2384.gif)



