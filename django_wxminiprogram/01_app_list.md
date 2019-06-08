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
- copy the sample from weui manual
- modify the image src, and the item name
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
                      <image class="weui-grid__icon" src="../../resources/icons/cube.svg" />
                      <view class="weui-grid__label">{{item.name}}</view>
                  </navigator>
              </block>
          </view>
      </view>
  </view>
  ```
### 2. menu.js
- because the Grid has many items, should define a variable in js file for iteration.
- define variable in the `data` filed which has been created by default
- this grid variabkle should be a list[] due to a list is iterable, and each item in this list should be a dict{}
  ```js
  data: {
    grid: [{"name": "app1"}, {"name": "appe"}]
  }
  ```
  - the `wx:for="{{grid}}"`, can iterate the number of the items in the variable `grid`
  - the `{{item.name}}` can get the value in the dict by its key in the grid list






