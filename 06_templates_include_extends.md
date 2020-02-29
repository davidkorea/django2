# 1.include

当多数页面公用一部分html代码时，可以将该部分代码提取出来作为单独的html代码块，放在templates目录下，然后在源文件中include该代码块

如果在include子模板中使用变量，可以受用with`{% include nav.html with username='hi' %}`，将一个变量传入

- 将公用的代码部分提取出来，作为 子代码块
- 将源文件作为 父元素，通过include来引如 子代码块

# 2. 模板继承 extends

- 将公用的代码部分提出出来，作为 父级元素
- 将每个页面自己的内容，作为 子元素，通过扩展extends子元素来将父模板引入

