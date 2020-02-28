
# django 模板

DTL， django template language，是django自带的模板语言，是一种带有特殊语法的html文件，可以传递参数进入，实现数据动态化，完成编译后生成一个普通html文件发送给客户端


## 1. 创建模板专用目录
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



## 2. 视图函数render后返回
```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```
- 由于在全局设置中指定了模板文件夹路径。此处直接填写文件名即可，无需指定路径
- render 就是将index.html先render_to_string，在用HttpResponse进行封装







