
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

> 开发者工具-设置-项目设置-不校验合法域名

注意Page函数中接收一个对象，所以函数创建的方式是`函数名：匿名函数(){ API }`
```javascript
wx.request({
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
```

```html
<view bindtap="testNetwork">tap me to test network</view>
```
```javascript
Page({
  testNetwork: function(){
    wx.request({
      url: 'http://www.davidkorea.com',
      method: 'GET',
      success: function (res) {
        console.log(res)
      },
      fail: function (res) {
        console.log('sorry...')
      },
    })
  },
})
```
<img width="850" src="https://user-images.githubusercontent.com/26485327/75221606-3661f600-57dd-11ea-98fb-86bcfb1d8617.png">

