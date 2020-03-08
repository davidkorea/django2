# 模型类中的Meta子类

- db_table
- ordering

```python
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=200, null=False)
    price = models.FloatField(null=False, default=0)  # default 默认值为0

    def __str__(self):
        return "<Book: (id:{id}, name:{name}, author:{author}, price:{price})>".format(
            id=self.id, name=self.name, author=self.author, price=self.price)

    class Meta:
        db_table = 'books'
        ordering = ['-price', 'id']
```
  - `ordering`接收一个数组，可以放多个排序字段
  - 添加负号`-`表示**倒序**
```python
# global urls.py
urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.order, name='order'),
]
```
```python
# book/views.py

def order(request):
    items = Book.objects.all()
    for i in items:
        print(i)
    return HttpResponse('ok')
```
```
// print: price降序，id升序
<Book: (id:19, name:MacBook, author:Apple, price:18990.0)>
<Book: (id:20, name:reactjs, author:david, price:88.0)>
<Book: (id:2, name:django web, author:david, price:66.0)>
```







