# 模板过滤器

- 自带过滤器
- 自定义过滤器

# 1. 自定义模板过滤器

1. 在某个app中创建一个Python Package，必须命名为`templatetags`，不得使用其他名字
2. 在`templatetags`下面创建python文件，用来放置自定义过过滤器
3. 在上面啊的python文件中，定义过滤器函数，该函数的第一个参数`value`是被过滤的那个值。需要时还可以在定义一个参数，但最多不能超过2各参数，除了value之外最多再创建一个参数
4. 写完了过滤器函数后，需要使用`django.template.Library.filter`注册
5. 还要把过滤器所在的app注册到全局settings.py的`INSTALLED_APPS`里面
6. 在模板html文件最开始使用load标签加载过滤器所在的python文件
