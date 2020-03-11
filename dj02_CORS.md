# 允许跨域访问

> React: Access to fetch at 'http://localhost:8000/api/' from origin 'http://localhost:1234' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.


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
