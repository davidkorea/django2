#  Object Relational Mapping （ORM）

- 采用原生sql，会在代码中出现大量的sql语句，且不可以复用
- 当数据库的一个字段改名后，那么代码中的几乎每一条原生sql语句都要改
- sql注入隐患

ORM 可以通过类的方式去操作数据库，因此**无需手动在数据库中创建表**，而是通过类来创建
- 表 -> 类
- 行 -> 实例
- 列 -> 属性


## 使用ORM创建一个数据库

1. 创建app，并添加值全局设置INSTALLED_APP中
2. 在创建的app中会自动生成models.py文件，用于创建ORM类
3. 将一个普通的python类变成一个可以映射数据到数据库的模型，需要继承django的models.Model父类
```python
from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=200, null=False)
    price = models.FloatField(null=False, default=0)  # default 默认值为0
```
4. `makemigrations` 生成迁移脚本文件
5. `migrate` 将迁移脚本文件映射到数据库
```shell
(dj3) yong@MacBookPro project8_orm % python manage.py makemigrations
Migrations for 'book':
  book/migrations/0001_initial.py
    - Create model Book
    
(dj3) yong@MacBookPro project8_orm % python manage.py migrate       
Operations to perform:
  Apply all migrations: admin, auth, book, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying book.0001_initial... OK
  Applying sessions.0001_initial... OK
```









