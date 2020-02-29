# include

当多数页面公用一部分html代码时，可以将该部分代码提取出来作为单独的html代码块，放在templates目录下，然后在源文件中include该代码块

如果在include子模板中使用变量，可以受用with`{% include nav.html with username='hi' %}`，将一个变量传入
