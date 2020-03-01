
# 模板中加载静态文件

静态文件如 css， js， jpg等文件，需要专门进行管理


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

3. 静态文件路径查找
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
  
  
  
