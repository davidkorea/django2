
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

#### - 语法
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

#### - Http请求的异步特性
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

-----

### 1.1.2 文件上传下载
```javascript
wx.uploadFile({
  url: '服务端地址',
  filePath: 'image1.png',
  name: 'file1',
  header: {},
  formData: {'user':'adminUser'},
  success: function(res) {},
  fail: function(res) {},
  complete: function(res) {},
})

wx.downloadFile({
  url: '',
  header: {},
  success: function(res) {},
  fail: function(res) {},
  complete: function(res) {},
})
```

#### 1.1.3 *task

由于网络请求的任务都是异步的，那么当这个任务提交之后，还需要对这个任务进行操作，需要使用

- Http请求 - Requesttask
- 上传文件请求 - UploadTask
- 下载文件请求 - DownloadTask
- socket请求 - SocketTask

拿到对应该任务的task后，可以进行的操作
- 中断任务，中途取消上传文件
- 触发回调函数，文件上传到10%的时候程序做什么，上传到20%的时候做什么
- 关闭链接，http请求或者是socket请求，关闭请求

-----

## 1.2 本地存储

将数据存储在 本地 缓存中 指定的 key中，数据存储生命周期和小程序本身一直（类似sessionStorage吧？）

- wx.setStorage，保存数据到指定key中
- wx.getStorage，根据key取出数据
- wx.removeStorage，根据key删除数据
- wx.clearStorage，慎用，清除掉本地所有缓存

### 1.2.1 setStorage & getStorage
> 异步请求
```html
<view bindtap="testNetwork">tap me to test network</view>
```
```javascript
Page({

testStoreage: function(){
    wx.setStorage({
      key: 'key1',
      data: 'value1',
      success: function(res) {
        console.log(res)
        console.log('store success')
      },
      fail: function(res) {},
      complete: function(res) {},
    })

    wx.getStorage({
      key: 'key1',
      success: function(res) {
        console.log('value of key1: ',res.data)
      },
    })
  },
})
```
<img width="753" src="https://user-images.githubusercontent.com/26485327/75226821-f6ecd700-57e7-11ea-9a76-98b437c9b178.png">

### 1.2.2 setStorageSync & getStorageSync
> 同步请求

- `wx.setStorageSync(key, data)`
- `var data = wx.getStorageSync(key)`

-----

## 1.3 文件系统
1. 全局文件管理器
2. 文件的增删改查
3. 文件夹的操作
### 1.3.1 全局文件管理器
获取全局唯一的文件管理器
```javascript
var fs = wx.getFileSystemManager()
```

### 1.3.2 文件的增删改查
fs是getFileSystemManager的对象
- `fs.saveFile`
- `fs.removeSavedFile`
- `fs.writeFile`
- `fs.readFile`
- `fs.appendFile`

### 1.3.3 文件夹的操作
fs是getFileSystemManager的对象
- `fs.mkdir` 
- `fs.rmdir` 
- `fs.isDirectory` 
- `fs.isFile` 


-----

# 2. 开放能力
## 2.1 用户数据
### 1. 头像、昵称等公开信息
wx.getUserInfo()

### 2. openid等敏感数据
openid用于识别不同用户，开发者不能直接使用

<img width="600" src="https://user-images.githubusercontent.com/26485327/75233270-8f3c8900-57f3-11ea-99c0-7f2be12c3697.png">

## 2. 推送消息
推送信息至服务号

## 3. 运营数据
- 小程序管理后台 - 统计
- 小程序数据助手 官方小程序

-----

# 3. 基础组件
WeUI-wxss https://github.com/Tencent/weui

- 样式文件可直接引用dist/style/weui.wxss
  - https://github.com/Tencent/weui-wxss/blob/master/dist/style/weui.wxss

- app.wxss
  ```css
  @import 'thirdparty/weui.wxss';
  ```
- 创建grids页面在pages目录下
  ```html
  <view class="page">
      <view class="page__hd">
          <view class="page__title">Grid</view>
          <view class="page__desc">九宫格</view>
      </view>
      <view class="page__bd">
          <view class="weui-grids">
              <block wx:for="{{grids}}" wx:key="*this">
                  <navigator url="" class="weui-grid" hover-class="weui-grid_active">
                      <image class="weui-grid__icon" src="../images/icon_tabbar.png" />
                      <view class="weui-grid__label">Grid</view>
                  </navigator>
              </block>
          </view>
      </view>
  </view>
  ```
  ```javascript
  Page({
      data: {
          grids: [0, 1, 2, 3, 4, 5, 6, 7, 8]
      }
  });
  ```
  








  
