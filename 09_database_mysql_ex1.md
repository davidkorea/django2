1. start project and app(front)
2. global settings
    - `__init__.py` import pymysql, `pymysql.install_as_MySQLdb()`
    - register app
    - templates, add html files when views function is created
    - static, add css / images when views function is created
    - disable crsf middle
    - urls, `from front import views`
3. Overview

| url | views function | template, extends base.html | DB|
|-|-|-|-|
| '' | index() | index.html | cursor.execute("select * from book") |
| add_book/ | add_book(name, author) | add_book.html | cursor.execute("insert into book(id,name,author)") |
| book_details/<int:book_id>/ | book_details(book_id) | book_details.html | cursor.execute("select * from book where id=book_id") |
| book_delete/<int:book_id>/ | book_delete(book_id) | null | cursor.execute("delete from book where id=book_id") |
    
    
    
    
3. app - front views.py functions
    - `index()`, render `index.html`
    - `add_book()`
    - `book_details()`
    - `book_delete()`
    










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






