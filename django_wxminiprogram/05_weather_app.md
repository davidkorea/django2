# Weather app implement
- change to classView
- wx weather page
- wx pulldown refresh

# 1. Django backend
## 1.1 weather classview
- if get weather by GET, should make a complicated url with ?
- only use POST to request juhe api, because write city names in request.body is easier.

```python
from django.views import View
from utils.response import CommonResponseMixin

class WeatherView(View, CommonResponseMixin):       # 继承View, CommonResponseMixin两个类
    def get(self, request):
        pass
        
    def post(self, request):
        data = []
        received_body = json.loads(request.body.decode('utf-8'))
        cities = received_body.get('cities')
        print(cities)
        for city in cities:
            result = juhe_api.weather(city.get('city'))     # 和wx前端配合，多一层获取city
            result['city_info'] = city                      # 将前端发来的信息，全部在保存在一个字段，返回回去
            data.append(result)
        data = self.wrap_json_response(data=data)
        return JsonResponse(data=data, safe=False)
```
- juhe api POST need request.body format:
    ```js
    {
        "cities": ["济南", "长沙"]
    }
    ```
- wx frontend pass the POST request.body format:
    ```js
    wx.request({
        url: app.globalData.serverUrl + app.globalData.apiVersion + 'service/weather/',
        method: "POST",
        data: {
                cities: [
                            {"province":"山东省", "city":"济南"},        
                            {"province":"湖南省", "city":"长沙"},
                        ]
              },
    })
    ```
- `json.loads(request.body.decode('utf-8'))` will get the json data
    ```js
    {
         cities: [
                    {"province":"山东省", "city":"济南"},        
                    {"province":"湖南省", "city":"长沙"},
                 ]
    }
    ```
    - thats why should` get('cities')` first to get the list []
    - then iterate the list [], and get the inner dict{} object, then `get('city')` in each of the inner dict{} object
    - cannot `get('cities').get('city')`, because `get('cities')` will get a list[]. which hs no get method
    - add a new culumn to save the inner dict{} which contains 'province' and 'city' to wx front for show the info on page
## 1.2 url
```python
from .views import weather

urlpatterns = [
    # path('weather/', weather.weather_app),
    path('weather/', weather.WeatherView.as_view()),
    ]
```
    
# 2. wx frontend
- create a dir anmed weather under pages path and create Page named weather

## 2.1 weather.wxml
```html
<view class="weui-panel weui-panel_access">
  <view wx:if='{{isAuthorized}}' class="weui-panel__hd">您关心的城市：</view>
  <view wx:else class="weui-panel__hd">当前热门城市：</view>
  <view class="weui-panel__bd">
      
    <navigator url="" wx:for='{{weatherData}}' wx:key="*this" class="weui-media-box weui-media-box_appmsg" hover-class="weui-cell_active">
      <view class="weui-media-box__hd weui-media-box__hd_in-appmsg">
            <image class="weui-media-box__thumb" src="../../resources/icons/weather/sunny.svg" />
      </view>
      <view class="weui-media-box__bd weui-media-box__bd_in-appmsg">
            <view class="weui-media-box__title">{{item.city_info.province}} - {{item.city}}</view>
          
            <view class="weui-media-box__desc">
                 <text>温度：{{item.temperature}}度 / 风况：{{item.wind_direction}} {{item.wind_strength}}</text>
            </view>
          
            <view class="weui-media-box__desc">
                <text>相对湿度：{{item.humidity}}</text>
            </view>
      </view>
    </navigator>
      
  </view>
</view>
```
## 2.2 weather.js
```js
const app = getApp()
const popularCities = [
  {"province": "山东省", "city": "济南" }, 
  {"province": "湖南省", "city": "长沙" }, 
  {"province": "北京市", "city": "北京" },
  {"province": "上海市", "city": "上海" }]

Page({
      data: {
            isAuthorized: false,
            weatherData: null
      },

     //生命周期函数--监听页面加载
      onLoad: function (options) {
            this.updateWeatherData()
      },

      updateWeatherData: function(){
            var that = this
            wx.showLoading({
                title: 'loading',
            })

            wx.request({
                  url: app.globalData.serverUrl + app.globalData.apiVersion + 'service/weather/',
                  method: "POST",
                  data: {
                        cities: popularCities
                  },
                  success: function(res){
                        var tempData = res.data.data    # 第二个data来自django返回的JsonResponse
                        that.setData({
                            weatherData: tempData
                        })
                        wx.hideLoading()
                  }
            })
      },
      
     //页面相关事件处理函数--监听用户下拉动作
      onPullDownRefresh: function () {      # 需要在weather.json中开启该功能
            this.updateWeatherData()    
      }
})
```
## 2.3 weather.json
```json
{
    "navigationBarTitleText": "天气",     # 配置页面名称     
    "enablePullDownRefresh": true         # 允许下拉页面自动刷新功能        
}
```

# 3. wx menu bingtap navigate page
## 3.1 menu.wxml
add  attributes `bindtap="onNavigatorTap" data-index="{{index}}"` to <navigator> tag
- when touch this  <navigator> element will call `onNavigatorTap()` function defined in js file
- `data-index="{{index}}`will pass the index of the select item of this grid. which can be got by `e.currentTarget.dataset.index` by the  `onNavigatorTap()` function
    
```html
<navigator url="" class="weui-grid" hover-class="weui-grid_active" bindtap="onNavigatorTap" data-index="{{index}}">
    <image class="weui-grid__icon" src="../../resources/icons/cube.svg" />
    <view class="weui-grid__label">{{item.app.name}}</view>
</navigator>
```
## 3.2 menu.js
```js
const app = getApp()
Page({
      // 页面的初始数据
      data: {
            grids: [
              { "name": "app1" },
              { "name": "app2" },
              { "name": "app3" }
            ]
      },

      // 生命周期函数--监听页面初次渲染完成
      onReady: function () {
            this.updateMenuData()
      },

      updateMenuData: function() {
            var that = this
            wx.request({
                  url: app.globalData.serverUrl + app.globalData.apiVersion + 'service/menu/',
                  success: function(res) {
                        var menuData = res.data.data
                        that.setData({
                             grids: menuData,
                        })
                  }
            })
      },

      onNavigatorTap: function(e){
            var index = e.currentTarget.dataset.index   # 从前端页面拿到所点击图标的idx
            var appItem = this.data.grids[index]        # 根据idx在grids数组中索引到相应的app
            if (appItem.app.application == 'weather'){  # 锁定相应app后，其内容与django后台的yaml一样
                  wx.navigateTo({
                        url: '../weather/weather',      # 跳转到weather页面
                  })
            }
      },
})
```
