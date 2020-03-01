

# database

1. install mysql
2. install navicat
3. set mysql db in django


# set mysql db in django

- settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',         # 数据库引擎
        'NAME': 'django_db1',                         # 数据库名
        'USER': 'root',
        'PASSWORD': '11111111',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}
```
<img width="950" src="https://user-images.githubusercontent.com/26485327/75625148-50913f00-5bf6-11ea-8d3f-ff1d45679840.png">
