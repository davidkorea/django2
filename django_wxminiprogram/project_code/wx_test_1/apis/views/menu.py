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


def get_menu(request):
    all_app_data = init_menu_data()
    published_app = all_app_data.get('published')
    # 可以直接返回这个信息，但不太友好还需要再增加几个字段
    wrap_response = response.wrap_json_response(data=published_app,
                                           code=response.ReturnCode.SUCCESS,)
    return JsonResponse(wrap_response, safe=False)