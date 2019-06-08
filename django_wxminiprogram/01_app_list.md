# Show app list in wxminiprogram by django backend

- create a yaml file as a list to identify published app and in developing app
- show developed app in wxminiprogram page as the yaml file recorded above
- this is easy to maintance the app list when a new app is developed
- the wxminiprogram show the app list by a grid weui

# 1. wxminiprogram
## 1.1 import weui.wxss and icon,img resources
- download https://github.com/Tencent/weui-wxss in the dist path
  - create a directory named as thirdparty, copy weui.wxss to this path
  - inport weui.wxss at the top of the global css file app.wxss 
    ```js
    @import "thirdparty/weui.wxss";
    ```
- create a derictory named as resources, copy the images and icon files into this path

## 1.2 create menu page
- create a directory named as menu under pages 
- create Page in the pages/menu dir
### 1. menu.wxml

### 2. menu.js
