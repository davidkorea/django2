from django.http import HttpResponse, JsonResponse, FileResponse
from thirdparty import juhe_api
import json
from django.views import View
from utils.response import CommonResponseMixin

class WeatherView(View, CommonResponseMixin):
    def get(self, request):
        # city = request.GET.get('city')
        # juhe_response = juhe_api.weather(city)
        # return JsonResponse(data=juhe_response, status=200)
        pass
        # if get weather by GET, should make a complicated url with ?
        # we only use POST to request juhe api, because write city names
        # in request.body is easier.

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


def weather_app(request):
    if request.method == 'GET':
        city =request.GET.get('city')
        juhe_response = juhe_api.weather(city)
        return JsonResponse(data=juhe_response, status=200)
    elif request.method == 'POST':
        received_body = json.loads(request.body)
        cities = received_body.get('cities')
        response = []
        for city in cities:
            result = juhe_api.weather(city)
            response.append(result)
        return JsonResponse(data=response, safe=False, status=200)