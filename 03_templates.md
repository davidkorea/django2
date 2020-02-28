
# django 模板

DTL， django template language，是django自带的模板语言，是一种带有特殊语法的html文件，可以传递参数进入，实现数据动态化，完成编译后生成一个普通html文件发送给客户端


## 1. 创建模板专用目录Python Package
- 在根目录，和爱她app平行的目录中，创建`templates` Python Package
- 添加该模板文件夹3全局设定中settings.py
  ```diff
  TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
   -    'DIRS': [],
   +    'DIRS': ['templates/'],
        'APP_DIRS': True,
        ...
    }
  ```
- 创建模板html文件index.html

## 2. 视图函数render后返回
```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```
- 由于在全局设置中指定了模板文件夹路径。此处直接填写文件名即可，无需指定路径
- render 就是将index.html先render_to_string，在用HttpResponse进行封装







