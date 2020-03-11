# 允许跨域访问

1. django venv中安装django-cors-headers
```python
pip install django-cors-headers

```

2. django全局设定
```diff
  INSTALLED_APPS = [
      ......
+     'corsheaders',
      ......
  ]

  MIDDLEWARE = [
      ......
+     'corsheaders.middleware.CorsMiddleware',
      ......
  ]

+ CORS_ORIGIN_ALLOW_ALL = True
+ CORS_ALLOW_CREDENTIALS = True
```
