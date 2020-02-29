# 1.include

当多数页面公用一部分html代码时，可以将该部分代码提取出来作为单独的html代码块，放在templates目录下，然后在源文件中include该代码块

如果在include子模板中使用变量，可以受用with`{% include nav.html with username='hi' %}`，将一个变量传入

- 将公用的代码部分提取出来，作为 子代码块
- 将源文件作为 父元素，通过include来引如 子代码块

# 2. 模板继承 extends

- 将公用的代码部分提出出来，作为 父级元素，如base.html
  - 在不同子页面需要添加各自不同代码的地方留出接口，并使用{% block blockName %}
    ```
    {% block content %}
    {% endblock %}
    ```
- 将每个页面自己的内容，作为 子元素，通过扩展extends子元素来将父模板引入
  - `{% extends 'base.html' %}`，必须在子页面的最上面添加该行代码，使其最为子页面的第一行代码
  - 第一行插入上面代码后，下面则使用在父页面留出的接口出使用{% block blockName %}
    ```
    {% block content %}
      my app contents...
    {% endblock %}
    ```
- views中的视图函数中`render(request, apppage.html, context=context)`，context的变量，可以直接在父模板中使用
  - 比如父模板base.html中，有一个变量`{{ username }}`
  - views里面的函数，在context中指定该变量usernaame
    ```python
    def index(request):
      context = {
        "username":"david"
      }
      return render(request, 'index.html', context=context)
    ```
  - 那么在子页面中使用extends扩展父页面时，父页面也可以使用上面视图函数中定义的变量的值


# 3. 模板继承 DEMO
- app
  - front app
  - book app
  - movie app
- 全局
  - urls
  - templates
    - base.html
    - front.html
    - book.html
    - movie.html

![Feb-29-2020 19-49-00](https://user-images.githubusercontent.com/26485327/75606898-91248600-5b2c-11ea-98a9-444f292bf810.gif)


## 3.1 全局设定

### 1. urls
由于多app，每个app的url具体细节由各自app内部的urls负责，全局urls使用include，并指定实例命名空间namespace
```python
from django.urls import path, include

urlpatterns = [
    path('', include('front.urls', namespace="front")),
    path('book/', include('book.urls', namespace="book")),
    path('movie/', include('movie.urls', namespace="movie")),
]
```

## 3.2 app设定

### 3.2.1 app - front
#### - urls
```python
from django.urls import path
from . import views

app_name = 'front'     // 由于使用实例命名空间，所以每个app都必须设定应用命名空间

urlpatterns = [
    path('', views.index, name="index")
]
```

#### - views
```python
from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'front.html', context=context)

```
### 3.2.2 app - book
#### - urls
```python
from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.index, name="index")   // 不同app之间，可以使用相同的url名称
]
```

#### - views
```python
from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'book.html', context=context)

```
### 3.3.3 app - movie

same as above

## 3.3 templates

使用模板继承的方式
1. 将相同的代码部分提取出来，作为父模板
3. 根据不同app，使用各自不同的代码来扩展extends父模板

#### - base
```html
 <div class="nav">
        <ul>              // 由于每个app都有使用index命名的url，所以必须通过namaespace进行区分
            <li><a href="{% url 'front:index' %}">front</a></li>
            <li><a href="{% url 'book:index' %}">book</a></li>
            <li><a href="{% url 'movie:index' %}">movie</a></li>
        </ul>
    </div>

    <div class="main">
        {% block main %}  // 其他页面来扩展extends该父模板时，会覆盖此内容
          main content    // 其他页面不添加该代码块时，将显示此处内容
        {% endblock %}
    </div>

    <div class="footer">
        <div>footer</div>
    </div>
```

#### - front
```python
{% extends 'base.html' %}

{% block main %}
<div>
    <p>this is the Front page main content</p>
</div>
{% endblock %}
```

#### - book
```python
{% extends 'base.html' %}

{% block main %}
<div>
    <p>this is the Book page main content</p>
</div>
{% endblock %}
```

#### - movie

same as above





