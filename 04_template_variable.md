
# 模板变量
1. if
2. for
3. with
4. url
5. spaceless
6. verbatim  逐字的(地)

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

<li><a href="{% url 'book_details' book_id='1' %}">book List</a></li>
```
- url名后面，空格，直接写参数名和参数值`book_id='1'`
- 传递多参数时，url中需要使用空格隔开`{% url 'book_details' book_id='1' category_id='12' %}`，不能使用逗号
```python
urlpatterns = [
    path('book/<book_id>/<category_id>/', views.book_details, name="book_details"),]

def book_details(request, book_id, category_id):
    text = 'the book id is: %s, category is: %s' % (book_id, category_id)
    return HttpResponse(text)
    
<li><a href="{% url 'book_details' book_id='1' category_id='12' %}">book List</a></li>
```

![Feb-29-2020 14-15-29](https://user-images.githubusercontent.com/26485327/75602197-f90fa800-5afd-11ea-9e72-22dfab1f0529.gif)


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


# 3. spaceless
分层次的html标签代码，选然后会生成一行没有空白字符的代码
```python
{% spaceless %}
  <div>
      <p>hello</p>
  </div>
{% endspaceless %}
```

```html
<div><p>hello</p></div>
```


# 4. autoescape 自动转义 {% autoescape off %}
- 默认开启了自动转义，将context中的内容，原封不动的显示在html文档中，以防止XSS漏洞
- 可以在模板中关闭自动转义`{% autoescape off %}`

```python
def index(request):
    context = {
        "link":"<a href='www.davidkorea.com'></a>"
    }
    return render(request, 'index.html', context=context)
```
```html
// templates/index.html
<p>{{ link }}</p>   // 完全被转义后，现实raw文本
```

<img width="700" src="https://user-images.githubusercontent.com/26485327/75602585-b4860b80-5b01-11ea-9ff1-f89952d1e785.png">

关闭自动转义
```python
context = {
      "link":"<a href='www.davidkorea.com'>website</a>"
  }
```
```html
// templates/index.html

{% autoescape off %}
    <p>{{ link }}</p>
{% endautoescape %}
```
<img width="700" src="https://user-images.githubusercontent.com/26485327/75602631-1e9eb080-5b02-11ea-9642-abc5d8d7ad28.png">


# 5. verbatim {% verbatim %}

当前端使用其他模板时，有些关键字会冲突，比如其他模板也是用{{}}来解析变量，需要让django不对其解析

`{% verbatim %}`中的`{{ }}` 和 `{%  %}`不会被django当做变量解析，而是让其他框架去解析








