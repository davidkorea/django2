
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


## 逻辑层
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
    - 通过`this.setData({'message':'hi world'})`
    
  - 使用全局数据
    - 首先获取App实例`const app = getApp()`
    - 在获取全局数据`var data = app.globalData`
    
- 页面声明周期
  - 页面启动时，一下两个线程同时启动
    - view thread
    - appService thread












