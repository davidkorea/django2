
- 微信API
  1. 网络请求
    - HTTP请求
    - 文件上传下载
    - *task 网络任务对象
  2. 本地存储
  3. 文件系统
- 开放能力
- 基础组件


# 1. 微信API
## 1.1 网络请求
#### HTTP请求
注意Page函数中接收一个对象，所以函数创建的方式是`函数名：匿名函数`
```javascript
Page({
  data: {
    msg: 'hello'
  },
  
  testNetwork: wx.request({
    url: '',
    data: '',
    header: {},
    method: 'GET',
    dataType: 'json',
    responseType: 'text',
    success: function(res) {},
    fail: function(res) {},
    complete: function(res) {},
  })
})
```
