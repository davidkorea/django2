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
    
    
    
    
    
