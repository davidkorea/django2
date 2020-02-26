
# 1. 目录介绍
配置文件类型
- `project.config.json`，工具配置，对微信开发者工具进行配置
- `app.json`，项目配置，页面路径，界面表现等等
- `<pageName>.json`，页面配置，对单个页面配置

pages目录
- 页面相关代码

utils目录
- 工具相关，网络请求，文件操作等 

其他目录
- thirdparty，components，resources

## 全局配置
- 全局入口 app.js
- 全局配置 app.json
  - pages，列表中的第一个元素默认为小程序首页
  - window，上端窗口样式，文字样式，配色等
  - tabbar，至少配置两个页面
- 全局样式 app.wxss

## 页面配置
会覆盖全局的window中的配置
- 开启下拉刷新`enablePullDownRefresh：true`

-----
# 2. 小程序框架

<img width="410" src="https://user-images.githubusercontent.com/26485327/75220168-bf772e00-57d9-11ea-88ea-d7f107a0ecdc.png">

<img width="410" src="https://user-images.githubusercontent.com/26485327/75219806-c6517100-57d8-11ea-95b1-de27a0d69e34.png">

## 2.1 逻辑层 js

> 数据，行为，路由

#### 小程序注册逻辑app.js
- App函数，全局唯一，只能调用一次。接收一个对象{}作为函数参数，里=里面包裹全局数据和声明周期函数
  ```javascript
    App({
      onLaunch(){}
      onShow(){}
      onHide(){}
      ...
      globalData:{}
    })
  ```
#### 页面注册逻辑
- page函数，和App类似
- 页面数据
  - data属性，所有页面数据都保存在data属性里，data是一个对象
    ```javascript
    data: {
      message: "hello world"
    }
    ```
    - 通过`this.data.message`即可获得属性对应的值
    - 通过`this.setData({'message':'hi world'})`更改数据的值
    - 这是逻辑层js文件中js的处理方法，在page界面里，data中的变量可以直接使用变量名message，而无需使用this.data.message
    
    
  - 使用全局数据
    - 首先获取App实例`const app = getApp()`
    - 在获取全局数据`var data = app.globalData`
    
- 页面生命周期
  - 页面启动时，一下两个线程同时启动
    - view thread
    - appService thread 
  <img width="510" src="https://user-images.githubusercontent.com/26485327/75216864-5a6b0a80-57d0-11ea-81a8-66427d535993.png">
  <img width="510" src="https://user-images.githubusercontent.com/26485327/75216866-5dfe9180-57d0-11ea-99fd-b85db5177275.png">

## 2.2 视图层 wxml wxss

> 结构，渲染，交互

#### 数据绑定
- 语法{{}}
```javascript
page({
  data: {
    message: 'hi wechat!',
  }
})
```
```html
<view>{{ message }}</view>
```


#### 列表渲染
- 语法`wx:for`
```javascript
Page({
  data: {
    message: "hi, wechat!",
    array: [{name:'foo'},{name:'bar'}]
  }
})
```
```html
<view wx:for="{{ array }}">{{index}}: {{item.name}} </view>
```
- **Page函数下的data中定义的变量，在wxml中直接调用变量名使用，而不是data.meaasge**
- index和item的写法由wx规定
- `index`，列表array中的索引
- `item.name`，对应列表中属性为name对应的值
<img width="247" src="https://user-images.githubusercontent.com/26485327/75218956-7671aa80-57d6-11ea-94b6-2a55998f0d88.png">


#### 条件渲染
- 语法`wx:if`,`wx:elif`,`wx:else`


#### 绑定事件

- 生命周期回调事件，不需要开发者认为绑定
- 页面绑定事件，需手动绑定

  <img width="510" src="https://user-images.githubusercontent.com/26485327/75219165-044d9580-57d7-11ea-9bc4-a5c7b88f2e00.png">

- 绑定事件的语法是以key value的形式存在
  - key， bind 或 catch 开头，然后跟上事件响应函数的名称
  
```html
<view bindtap="tapme">tap me</view>
```
```javascript
page({
  data: {
    msg: 'hello',
  },
  tapme: function(e){
    console.log(e)
  },
})
```
```
{type: "tap", timeStamp: 4548, target: {…}, currentTarget: {…}, detail: {…}, …}changedTouches: [{…}]currentTarget: {id: "", offsetLeft: 134, offsetTop: 421, dataset: {…}}detail: {x: 175.28646850585938, y: 435.1927490234375}target: {id: "", offsetLeft: 134, offsetTop: 421, dataset: {…}}timeStamp: 4548touches: [{…}]type: "tap"_requireActive: true__proto__: Object
```
- 由于页面js里面的Page函数接收的是一个对象，因此虽有变量和函数都是以键值对的形式存在，事件函数也是
  - `函数名: 匿名函数`的方式进行，而不能`function eventName（){}`直接声明一个函数















