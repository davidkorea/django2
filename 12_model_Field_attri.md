# Field属性

## 1. null
- CharField， TextField 等文本类型数据不建议允许使用空值`null=True`
  - 因为文本类型字段，默认`null=False`，如果创建数据时，没有给改字段赋值，那么数据库中自动插入一个空字符串`""`，而不是真正的NULL
  - 所以之后使用数据时，会出现混淆
- 真正设置`null=True`时，在数据库中存储空值，数据库会显示`(NULL)`

<img width="200" alt="截屏2020-03-08下午2 58 50" src="https://user-images.githubusercontent.com/26485327/76158120-54b8e180-614d-11ea-8677-f371e5a7b124.png">

## 2. blank
不作用于数据库层面，而是用于表单提交时的验证

## 3。 db_column
指定存到数据库中某个字段的名称
```python

class User(models.Model):
  age = models.IntegerField(db_column='user_age')
```

- 项目中的代码变量为age
- 实际存储到数据库的字段名为user_age

## 4. default
数据保存到数据库时，如果没有特别指定，则给改字段设置默认值
```python

class User(models.Model):
  age = models.IntegerField(db_column='user_age', default=0)
```
- default除了设定一个确定的数值，还可以设置一个函数，如`default=now`，now()函数import from django.utils.datetime


## 5. primary_key
- 主键


## 6. unique

- 手机号，邮箱一般不设置为主键，但是一般设置为unique唯一

<img width="400" src="https://user-images.githubusercontent.com/26485327/76158263-f12fb380-614e-11ea-98ff-f7a5f504f43a.png">


## 7. 其他
- choices
- db_index
- editable
- error_messages
- help_text
- ...








