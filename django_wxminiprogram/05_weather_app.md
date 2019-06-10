# 实现天气应用
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

class WeatherView(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        data = []
        received_body = json.loads(request.body.decode('utf-8'))
        cities = received_body.get('cities')
        print(cities)
        for city in cities:
            result = juhe_api.weather(city.get('city'))
            result['city_info'] = city
            data.append(result)
        data = self.wrap_json_response(data=data)
        return JsonResponse(data=data, safe=False)
```
