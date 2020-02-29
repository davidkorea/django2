
# 模板变量
1. if
2. for
3. with





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

```python
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












