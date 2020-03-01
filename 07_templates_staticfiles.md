
# 模板中加载静态文件

静态文件如 css， js， jpg等文件，需要专门进行管理

# 1. 检查全局设定
1. 全局settings.py **INSTALLED_APPS**，`django.contrib.staticfiles`，创建项目后已自动添加
```python
INSTALLED_APPS = [
    'django.contrib.staticfiles',
]
```
2. 全局settings.py **STATIC_URL**，`/static/`，创建项目后已自动添加
```python
STATIC_URL = '/static/'
```
- 设置请求静态文件时的路径：hostname/static.1.png
# 2. 静态文件路径查找

### 2.1 [不常用]静态文件app内路径查找
  - 将app注册到全局settings.py的INSTALLED_APPS中
  ```python
  INSTALLED_APPS = [
      'django.contrib.staticfiles',
      'front',
      'book',
      'movie'
  ]
  ```
  - 在app目录下创建文件夹，必须命名为`static`
  - 为了防止不同app下的static文件中存在相同名的静态文件，需要在各自app的static文件夹中在创建一个以自己app名字为名的子文件夹，如book app的情况使用`static/book`
  - 在模板html文件中引用静态文件，文件开头使用`{% load static %}`，需要引用静态文件时`{% static 'front/1.png' %}`
  ```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
            <img src="{% static 'front/1.png' %}" alt="">
        </body>
    </html>  
  ```
  
### 2.2 [常用]静态文件全局路径查找
  
在全局settings.py中指定一个单独的路径，来全权负载静态文件的管理，而不用分散于各个app的内部，这样统一管玻更方便

- 在全局设定中添加`STATICFILES_DIRS`
```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```
- 在根目录下，即app的平行目录下，创建文件夹`static`

在全局static文件夹下创建css文件，并引用3模板文件中
```css
// static/base.css
body {
    background-color: thistle;
}
```
```html
// templates/iondex.html

{% load static %}           // 必须首航开启加载静态文件
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="{% static 'base.css' %}">  // 引用全局静态文件
</head>
<body>
    <img src="{% static 'front/1.png' %}" alt="">       // 同样可以使用app内部的静态文件
</body>
</html>
```

# 3. 简化{% load static %}

- 由于static标签不是像if和for一样的django内置标签，因此每个模板页面的首行都要有{% load static %}，这样太麻烦了
- 手动吧static标签设置为内置标签，这样以后再使用，直接`{% static 'static file' %}`即可，而无需在首行添加上面的标签
- 全局settings.py中的**TEMPLATES** 的OPTIONS中添加`'builtins': ['django.templatetags.static']`
```diff
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
+           'builtins': ['django.templatetags.static'],
        },
    },
]

```





