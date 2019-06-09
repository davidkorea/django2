import requests

def weather(city):
    juhe_api = 'http://apis.juhe.cn/simpleWeather/query'
    key = '649c2db566afdf6c7137ff9ca2a99f95'
    param= '?city={}&key={}'.format(city, key)
    query_url = juhe_api + param
    print(query_url)
    request = requests.get(url=query_url)
    # json_data = json.loads(request.text)
    json_data = request.json()
    result = json_data.get('result')
    data = {}
    data['city'] = result.get('city')
    data['temperature'] = result.get('realtime').get('temperature')
    data['wind_direction'] = result.get('realtime').get('direct')
    data['wind_strength'] = result.get('realtime').get('power')
    data['humidity'] = result.get('realtime').get('humidity')  # 湿度
    return data

# weather('济南')