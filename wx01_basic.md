
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
- 小程序注册逻辑app.js
  - ```App({
    onLaunch(){}
    onShow(){}
    onHide(){}
    ...
    globalData:{}
  })
  `

- 页面注册逻辑



