
- 已创建的数据表中添加新字段，需要给新字段设置默认值default，否则执行makemigration时报错
  - 因为数据表中已有的数据，以前并没有这个新字段对应的值，当添加了新字段后，数据库不知道要给之前的数据如何添加这个新字段的值
  - 因此需要给之前的数据指定的新字段的值
  

# 1. 模型常用属性
- AutoField，int形，自增长
- BigAutoField, 64为的AutoField，功能同上
- BooleanField
  - python中使用后True和False
  - 数据库中对应显示为1和0
  - 若允许boolean字段为空值，即像设置`BooleanField(null=True)`，则需要使用**NullBooleanField**来代替
  
- CharField，可变长度字符串
  - 此类型必须要指定`max_length`参数，否则报错
  - 如果长度超过254个字符，这不建议使用CharField，而是使用**TextField**来存储长文本

# 2. 时间相关模型属性
##### 1. Time Basics
##### 2. ORM time Field
- `models.DateTimeField`， 年月日时分秒
- `models.DateField`， 年月日
- `models.TimeField`， 时分秒
  

## 2.1 Time Basics
1. Python Time Basics
2. django Time Basics

### 2.1.1 Python Time Basics
> - naive time, 不知道当前时间所处时区
> - aware time，直到当前时间表示的是哪个时区的时间

1. pytz， python-venv中安装django后，会自动安装一个pytz的库，用来处理时区
2. pytz中的astimezone方法，将一个时区的时间转为另一个时区的时间，这个方法只能被aware time类型的时间调用，不能被naive time类型的时间调用
    - 目前windows和MAC已经做了优化，naive和aware都可以适用，但是linux还不可以

```python
from datetime import datetime
import pytz

now = datetime.now()               # navie time
utc_tz = pytz.timezone('UTC')      # 创建一个时区 对象

utc_now = now.astimezone(utc_tz)   # 将当前时间now转换为UTC时区的时间
>> ValueError: astimezone() cannot be applied to naive datetime.   # 报错

now = now.replace(tzinfo=pytz.timezone('Asia/Shanghai'))  # 将当前时间设置时区为中国上海，aware time
utc_now = now.astimezone(utc_tz)   # 此时可以正确转化
```



### 2.1.2 django 时间
#### 1. from django.utils.timezone import now
```python
# global settings.py

USE_TZ = True   # 默认开启，即设置时间为aware time, False为naive time
```

```python
# now()源码

def now():
    """
    Return an aware or naive datetime.datetime, depending on settings.USE_TZ.
    """
    if settings.USE_TZ:     # 全局设定USE_TZ为True
        # timeit shows that datetime.now(tz=utc) is 24% slower
        return datetime.utcnow().replace(tzinfo=utc)    # 返回UTC时间，而不是东八区中国的时间
    else:
        return datetime.now()
```
- django的now()函数不同于python自带的now()函数
- 全局设定USE_TZ为True后。**now()函数返回UTC时间（英国格林尼治时间），而不是东八区中国时间**

#### 2. from django.utils.timezone import localtime

```python
# global settings.py

TIME_ZONE = 'Asia/Shanghai'  # 两个选项配合使用，TIME_ZONE默认为UTC，即格林尼治时间
USE_TZ = True 
```
```python
def localtime(value=None, timezone=None):
    """
    Convert an aware datetime.datetime to local time.
    Only aware datetimes are allowed. When value is omitted, it defaults to
    now().
    Local time is defined by the current time zone, unless another time zone
    is specified.
    """
    if value is None:
        value = now()
    if timezone is None:
        timezone = get_current_timezone()
    # Emulate the behavior of astimezone() on Python < 3.6.
    if is_naive(value):
        raise ValueError("localtime() cannot be applied to a naive datetime")
    return value.astimezone(timezone)
```
- 根据全局设定中的TIME_ZONE，返回当前时区的时间



## 2.2 示例

```python
# book/models.py

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    removed = models.BooleanField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
```
```python
# book/views.py

from .models import Article

def index(request):
    ariticle = Article(name='django web', removed=False)
    ariticle.save()
    return HttpResponse('ok')
```
<img width="672" src="https://user-images.githubusercontent.com/26485327/76157598-baa16b00-6145-11ea-993e-68b4190b860e.png">

- `create_time = models.DateTimeField(auto_now_add=True)`
  - auto_now_add 第一次创建是，自动添加UTC时间，因为全局设定中`USE_TZ=True`
- `update_date = models.DateTimeField(auto_now=True)`
  - 每次更新数据，此处自动添加最后一次更新数据的时间
  
  
 ```python
# book/views.py

from .models import Article
def index(request):
    # ariticle = Article(name='django web', removed=False)
    article = Article.objects.get(pk=1)
    article.name = 'learn django'
    article.save()
    return HttpResponse('ok')
``` 
  
  
![Mar-08-2020 14-09-21](https://user-images.githubusercontent.com/26485327/76157648-71055000-6146-11ea-9ae2-29ede7185677.gif)
<img width="594" src="https://user-images.githubusercontent.com/26485327/76157660-909c7880-6146-11ea-8615-54f9fbefb7ec.png">

- 更新该条数据后，create时间没有变化，开启auto_now的update时间变化了



  









