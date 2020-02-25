
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
> 开发者工具-设置-项目设置-不校验合法域名

### 1.1.1 HTTP请求

#### 语法
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
        console.log(res.data)  // 网址对应的原始html代码
      },
      fail: function (res) {
        console.log('sorry...')
      },
    })
  },
})
```
<img width="840" src="https://user-images.githubusercontent.com/26485327/75221606-3661f600-57dd-11ea-98fb-86bcfb1d8617.png">
<img width="840" src="https://user-images.githubusercontent.com/26485327/75223027-855d5a80-57e0-11ea-9c9c-7bafcb27eb2c.png">

## Http请求的异步特性
- wx.request请求发送至后就完成了，不管返回是success还是fail，也不管什么时候返回结果
  - 直接执行后面的过程
  - 什么时候http的请求结果回来了，成功就调用success，失败就调用fial
  
```javascript
testNetwork: function(){
  var data = undefined                      // http请求之前创建变量
  wx.request({
    url: 'http://www.davidkorea.com',
    method: 'GET',
    success: function (res) {
      console.log('http request success')
      data = res.data                       // 请求成功的data赋值给前面定义的变量
    },
    fail: function (res) {
      console.log('sorry...')
    },
  })
  console.log(data)                         // 输出变量
},
```
<img width="756" src="https://user-images.githubusercontent.com/26485327/75223765-1da80f00-57e2-11ea-93c4-2d512ae224be.png">

- 先输出了 值为undefined的data变量，之后输出了成功调用
- 因为在http请求拿到成功返回的结果之前，程序没有等待，而是执行了下面的代码
- 也就是在成功拿到http的返回值之前，变量data没有被赋值，因此还是undefined














