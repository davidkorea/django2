
# django 模板

DTL， django template language，是django自带的模板语言，是一种带有特殊语法的html文件，可以传递参数进入，实现数据动态化，完成编译后生成一个普通html文件发送给客户端


# 1. 创建模板专用目录
### 1.1 全局模板路径
- 在根目录，和爱她app平行的目录中，创建`templates`，创建目录即可，无需床架安Python Package
- 添加该模板文件夹3全局设定中settings.py
  ```diff
  TEMPLATES = [
     {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
  -     'DIRS': [],
  -     'DIRS': ['templates/'],
  +     'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        ...
     }
  ```
- 创建模板html文件index.html
### 1.2 app目录下创建templates
在app目录下，创建directory目录templates，必须是这个名字，不能自定义。并创建index.html

- 在全局设定中，不填写`TEMPLATES的DIRS`，而是将`APP_DIRS`设置为`True`，django将在app目录下寻找模板文件
- 同时需要设定的时，将创建的app注册到`INSTALLED_APPS = [ ]`中才可以

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'front'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],           // 留空
        'APP_DIRS': True,
        ...
    }
```
### 1.3 模板文件查找顺序
优先级
1. DIRS
2. APP_DIRS，当先app下templates
3. APP_DIRS，其他已安装在INSTALLED_APPS中的app目录下的templates



# 2. 视图函数render后返回
```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```
- 由于在全局设置中指定了模板文件夹路径。此处直接填写文件名即可，无需指定路径
- render 就是将index.html先render_to_string，在用HttpResponse进行封装


# 3. 模板变量
- 在模板中使用变量，需要使用两个花括号 `{{  }}`
- 访问对象（类class）的属性，可以通过`变量.属性名`的方式获得属性值
- 访问字典的key对应的value，使用`字典.key名`的方式获得对应key的属性值value，不能通过dict[key]的方式，因为不能使用方括号`[ ]`
  - 不能在字典中，把python dict的关键字用作键名，如keys，values，items，否则会出现问题
  - 否则，当访问`dict.keys`时，返回的将不是字典的所有键，而是这个
- 访问数组或元素，也是通过点的方式获得`list.0`,，不能通过方括号获得`list[0]`，这与原生python不一样

## 3.1 {% if %} {% elif %} {% else %} {% endif %}

```python
// vires.py
from django.shortcuts import render

def index(request):
    context = {
        'books':['三国','水浒','红楼']
    }
    return render(request,'index.html', context=context)
```
```xml
<div>
    {% if "三国" in books %}
        <p>三国</p>
    {% else %}
        <p>no</p>
    {% endif %}
</div>
```

## 3.2 {% for i in list %}{% endfor %}
### 1. 遍历列表
```python
def index(request):
    context = {
        'books':['三国','水浒','红楼']
    }
    return render(request,'index.html', context=context)
```
```python
<ul>
    {% for book in books reversed %}
        <li>{{ book }}</li>
    {% endfor %}
</ul>
```
- reversed 倒序

### 2. 遍历字典
```python
context = {
    'persons':{
        "username":'david',
        "age":'22'
    }
}
```
```python
<div>
    {% for key,value in persons.items %}
        <div>{{key}} : {{value}}</div>
    {% endfor %}
</div>
```
### 3. forloop.counter

```python
context = {
    'books':[{
        "name":"三国演义",
        "author":"罗贯中",
        "price":120
    },{
        "name": "水浒传",
        "author": "施耐庵",
        "price": 109
    },{
        "name": "西游记",
        "author": "吴承恩",
        "price": 99
    },{
        "name": "红楼梦",
        "author": "曹雪芹",
        "price": 199
    }],
```
```python
<table>
    <thead>
        <tr>
            <td>Item</td>
            <td>Name</td>
            <td>Author</td>
            <td>Price</td>
        </tr>
    </thead>
    <tbody>
        {% for book in books %}
            <tr>
                <td>{{ forloop.counter }}</td>
                <td>{{book.name}}</td>
                <td>{{book.author}}</td>
                <td>{{book.price}}</td>
            </tr>
        {% endfor %}
    </tbody>
</table>
```
<img width="200" src="https://user-images.githubusercontent.com/26485327/75598279-8f7ba380-5ad5-11ea-89e6-f6d9f77a6ede.png">

- `loop.counter`, 1 -> n
- `loop.counter0`, 0 -> n
- `loop.revcounter`, n -> 1
- `loop.revcounter0`, n -> 0
- `loop.first`, 第一次遍历 
- `loop.last`, 最后一次遍历


```python
<tbody>
    {% for book in books %}
        {% if forloop.first %}
            <tr style="background-color:aliceblue">
        {% elif forloop.last %}
            <tr style="background-color:darkgray;color:white">
        {% else %}
            <tr>
        {% endif %}   // 仅开始标签根据条件变化，闭合标签在最后保持不变
                <td>{{ forloop.counter }}</td>
                <td>{{book.name}}</td>
                <td>{{book.author}}</td>
                <td>{{book.price}}</td>
            </tr>     // 闭合标签不变
    {% endfor %}
</tbody>
```
<img width="200" src="https://user-images.githubusercontent.com/26485327/75598531-40367280-5ad7-11ea-9686-69108374162c.png">







