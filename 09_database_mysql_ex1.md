


# 1. Form

## 1.1 crsf
```html
<form action="" method="POST">
  <input type="text" name="name">
  <input type="submit"m value="Submit">
</form>
```
<img width="677" src="https://user-images.githubusercontent.com/26485327/75646974-5c2c4680-5c86-11ea-80df-64203ac3a65b.png">

```python
// global settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
## 1.2 取消输入框历史记录提示
`autocomplete="off"`

```html
<form action="" method="POST" autocomplete="off>
  <input type="text" name="name">
  <input type="submit"m value="Submit">
</form>
```






