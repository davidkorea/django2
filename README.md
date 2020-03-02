



- Web服务器
  - 负责处理http请求，响应静态文件，常见由apach，nginx，iis
- 应用服务器
  - 负责处理逻辑的服务器，如python代码是不能通过ngnix这种web服务器来执行，只能通过应用服务器进行处理
  - 常见由python的uwsgi，java的tomcat等
- Web应用框架
  - 使用一种语言，封装了常用的Web功能的框架，jdango，flask等

**浏览器 -> Web服务器ngnix -> 应用服务器python -> Web框架django**

-----

- [anaconda3初始安装设置terminal环境变量 #1](https://github.com/davidkorea/django2/issues/1#issue-571842494)
- [python venv, virtualenv, virtualenvwrapper 虚拟环境比较 #2](https://github.com/davidkorea/django2/issues/2#issue-571906883)
- [创建一个django项目 Pycharm配置编译环境interpreter #3](https://github.com/davidkorea/django2/issues/3#issue-571912084)
- [django2/3 mysqlclient pymysql "Error loading MySQLdb module. Did you install mysqlclient?" #5](https://github.com/davidkorea/django2/issues/5#issue-573657976)
-----


- dj01
  - 安装anaconda，设置环境变量
  - 安装python虚拟环境virtualenv
  - 启动django项目
