from django.http import HttpResponse, JsonResponse, Http404, FileResponse
from wx_test_1 import settings
import os
from utils import response
from django.views import View
import hashlib

def image(request):
    # return a piece of image
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        img_file = os.path.join(settings.IMAGE_PATH, md5 + '.jpg')
        if not os.path.exists(img_file):
            return Http404()
        else:
            data = open(img_file, 'rb').read()
            # return HttpResponse(content=data, content_type='image/jpg')
            return FileResponse(open(img_file, 'rb'), content_type='image/jpg')

class ImageView(View, response.CommonResponseMixin):
    def get(self, request):
        md5 = request.GET.get('md5')
        img_file = os.path.join(settings.IMAGE_PATH, md5 + '.jpg')
        if not os.path.exists(img_file):
            return Http404()
        else:
            data = open(img_file, 'rb').read()
            # return HttpResponse(content=data, content_type='image/jpg')
            return FileResponse(open(img_file, 'rb'), content_type='image/jpg')

    def post(self,request):
        files = request.FILES
        response_data = []
        for k, v in files.items():
            file_content = v.read()
            md5 = hashlib.md5(file_content).hexdigest()
            save_file_path = os.path.join(settings.IMAGE_PATH, md5 + '.jpg')
            with open(save_file_path, 'wb') as f:
                f.write(file_content)
            response_data.append({
                "name": k,
                "md5": md5  # pass to frontend
            })
        message = 'post success.'
        response_data = self.wrap_json_response(data=response_data,
                                                message=message)
        return JsonResponse(data=response_data, safe=False)

    def delete(self,request):
        md5 = request.GET.get('md5') # 从请求的url中get出md5
        file_name = md5 + '.jpg'
        file_path = os.path.join(settings.IMAGE_PATH, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            message = 'remove success.'
        else:
            message = 'file %s not found.' % file_name
        response_data = self.wrap_json_response(message=message)
        return JsonResponse(data=response_data, safe=False)


    def put(self, request):
        message = 'put success.'
        response_data = self.wrap_json_response(message=message)
        return JsonResponse(data=response_data, safe=False)





def image_test(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        img_file = os.path.join(settings.IMAGE_PATH, md5 + '.jpg')
        if not os.path.exists(img_file):
            return response.wrap_json_response(
                code=response.ReturnCode.RESOURCE_NOT_EXIST)
        else:
            response_data = {}
            response_data['name'] = md5 + '.jpg'
            response_data['url'] = '/service/image/?md5=%s' % (md5)
            data = response.wrap_json_response(data=response_data)
            return JsonResponse(data=data, safe=False)