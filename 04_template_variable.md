
# 模板变量
1. if
2. for
3. with





# 1. {% with %}{% endwith %}
定义的变量只能在with语块里面使用

```
context = {
  "persons":['david','davidson'],
}
```
```python
<div>
    {% with da=persons.0 %}   // 等号两边不能有空格
        <p>{{ da }}</p>
    {% endwith %}
</div>
```
或
```python
<div>
    {% with persons.0 as da %}  
        <p>{{ da }}</p>
    {% endwith %}
</div>
```






















