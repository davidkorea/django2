# 图片备份应用
- 图文消息实战
- django文件上传与下载
  - 小程序上传文件调用POST方法，django后台从request中取出上传的文件，本存在后台服务器本地（AWS S3？）
    - 获取请求内容`request.FILES`，会的一个key-value对象，key=文件名，上传时指定， value=文件对象/文件本身二进制内容
  - 小程序发起DELETE请求时，在后台服务器使用DELETE方法删除文件
  
- 小程序文件上传与下载
  - weui uploader
    ![](https://i.loli.net/2019/06/09/5cfca0bb9601c71372.png)
# 1. UploadFiles
## 1.1 django
- image view POST method
  ```python
  import hashlib

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
          files = request.FILES   # wxapp的POSTrequest中通过request.FILES获取格式为key-value的上传文件
          response_data = []
          for k, v in files.items():
              file_content = v.read()     # 读取为二进制文件
              md5 = hashlib.md5(file_content).hexdigest()
              save_file_path = os.path.join(settings.IMAGE_PATH, md5 + '.jpg')  # 为文件创建路径/空白文件
              with open(save_file_path, 'wb') as f:   # 打开这个空白文件
                  f.write(file_content)   # 将读取到的二进制文件写入上面创建的空白文件路径中
              response_data.append({
                  "name": k,    # key为上传时指定文件名
                  "md5": md5    # 将保存后的文件的文件名md5也传给前端
              })
          message = 'post success.'
          response_data = self.wrap_json_response(data=response_data,
                                                  message=message)
          return JsonResponse(data=response_data, safe=False)
  ```
