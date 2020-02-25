
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


# 2. 逻辑层
### 小程序注册逻辑app.js
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
### 页面注册逻辑
- page函数，和App类似
- 页面数据
  - data属性，所有页面数据都保存在data属性里，data是一个对象
    ```javascript
    data: {
      message: "hello world"
    }
    ```
    - 通过`this.data.message`即可获得属性对应的值
    - 通过`this.setData({'message':'hi world'})`
    
  - 使用全局数据
    - 首先获取App实例`const app = getApp()`
    - 在获取全局数据`var data = app.globalData`
    
- 页面声明周期
  - 页面启动时，一下两个线程同时启动
    - view thread
    - appService thread 
  <img width="517" src="https://user-images.githubusercontent.com/26485327/75216864-5a6b0a80-57d0-11ea-81a8-66427d535993.png">
  <img width="517" src="https://user-images.githubusercontent.com/26485327/75216866-5dfe9180-57d0-11ea-99fd-b85db5177275.png">

# 3. 视图层

结构，渲染，交互

### 数据绑定
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


### 列表渲染
- 语法`wx:for`
  ```javascript
  page({
    data: {
      message: "hi, wechat!",
      array: [{name:'foo'},{name:'bar'}]
    }
  })
  ```
  ```html
  <view wx:for="{{ array }}">{{index}}: {{item.name}} </view>
  ```
  - `index`，列表array中的索引
  - `item.name`，对应列表中属性为name对应的值
  <img width="247" src="https://user-images.githubusercontent.com/26485327/75218956-7671aa80-57d6-11ea-94b6-2a55998f0d88.png">








### 条件渲染
### 绑定事件
















