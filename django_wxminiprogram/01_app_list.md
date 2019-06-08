# Show app list in wxminiprogram by django backend

- create a yaml file as a list to identify published app and in developing app
- show developed app in wxminiprogram page as the yaml file recorded above
- this is easy to maintance the app list when a new app is developed
- the wxminiprogram show the app list by a grid weui

# 1. Static wx page
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
- add the menu page to app.json `tabbar`
  ```js
  {
  "pagePath": "pages/menu/menu",
  "text": "menu"
  }
  ```
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
  - **what we will do is that make this menu page can get the app list automatically from the django backend instead of the static fake grid list.**


# 2. Back-end: django
- create a ymal file to write the published app and developing app list
- let django read this file and provide a HTTPresponse api for front-end request
- when developed a new app, modify th9is yaml file and wxminiprogram can automatically get this app name in the menu page
## 2.1 yaml 
- wxminiprogram should read published -> app -> name, similiar as read a json 
  ```yaml
  published:
    - app:
        category: life
        application: weather
        name: 天气
        publish_date: 2019-06-08
        url: /service/weather
        desc: this is a weather app.
    - app:

  developing:
    - app:
  ```

## 2.2 menu view
- create a  function to read this yaml file and another function to warp a costomized Jsonresponse
### 1. create utils to wrap a costomized Jsonresponse
- create a PythonPackage named as utils and create a py file named as response.py
  ```python
  class ReturnCode:
      # 状态码
      SUCCESS = 0
      FAILED = -100
      UNAUTHORIZED = -500
      BROKEN_AUTHORIZED_DATA = -501
      WRONG_PARAMS = -101

      @classmethod
      def message(cls, code):
          # 根据状态码转换成说明文字
          if code == cls.SUCCESS:
              return 'success'
          elif code == cls.FAILED:
              return 'failed'
          elif code == cls.UNAUTHORIZED:
              return 'unauthorized'
          elif code == cls.WRONG_PARAMS:
              return 'wrong_params'
          else:
              return ''

  def wrap_json_response(data=None, code=None, message=None):
      # 将一个Jsonresponse，再包装上code和message两个信息
      # return一个dict结构，再有safe=false读取将一个Jsonresponse
      response = {}
      if not code:
          code = ReturnCode.SUCCESS
      if not message:
          message = ReturnCode.message(code)
      if data:
          response['data'] = data
      response['code'] = code
      response['message'] = message
      return response
  ```

### 2. create a menu view in the apis app
/Users/david/PycharmProjects/wx_test_1/apis/views/weather.py
```python
from django.http import JsonResponse
import os
import yaml
from wx_test_1 import settings
from utils import response

def init_menu_data():
    app_yaml_file = os.path.join(settings.BASE_DIR, 'app.yaml')
    with open(app_yaml_file, 'r', encoding='utf-8') as f:
        apps = yaml.load(f)
        return apps
        # 用于读取yaml文件，并未下个函数提供原始数据

def get_menu(request):
    all_app_data = init_menu_data()
    published_app = all_app_data.get('published')
    # 可以直接返回这个信息，就是上面函数的读取的yaml原始信息，但不太友好还需要再增加几个字段
    wrap_response = response.wrap_json_response(data=published_app,
                                                code=response.ReturnCode.SUCCESS,)
    return JsonResponse(wrap_response, safe=False)
```
### 3. urls
```python
path('menu/', menu.get_menu)from .views import weather, menu

urlpatterns = [
    # path('', weather.weather_app),
    path('weather/', weather.weather_app),
    path('menu/', menu.get_menu)
]
```


