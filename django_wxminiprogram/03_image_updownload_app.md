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
## 1.1 django backend
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
## 1.2 wx frontend
- create a directory named as imgbackup
- create Page named as imgbackup
- copy and modify weui uploader wxml and js code, add buttons 
### 1.2.1 imgbackup.wxml
```html
<view class="page">
  <view class="page__bd">
    <view class="weui-cells">
      <view class="weui-cell">
          <view class="weui-cell__bd">
              <view class="weui-uploader">
                  <view class="weui-uploader__hd">
                      <view class="weui-uploader__title">上传图片</view>
                  </view>
                  <view class="weui-uploader__bd">
                      <view class="weui-uploader__files" id="uploaderFiles">

                          <block wx:for="{{needUploadFiles}}" wx:key="*this">
                              # 循环已选择的待上传文件列表，如果为空，则不显示
                              <view class="weui-uploader__file" bindtap="previewImage" id="{{item}}">
                                  # 如果有待上传图片，显示，并绑定点击事件previewImage，用与放大全屏显示
                                  <image class="weui-uploader__img" src="{{item}}" mode="aspectFill" />
                                      # 显示待上传图片，chooseImage api的tempFilePath可作为img标签的src属性显示图片
                              </view>

                          </block>

                      </view>

                      <view class="weui-uploader__input-box">

                          <view class="weui-uploader__input" bindtap="chooseImage"></view>

                      </view>
                  </view>
              </view>
          </view>
      </view>
    </view>
    <view class="page__bd page__bd_spacing">
      <button class="weui-btn" type="primary" bindtap='uploadFiles'>Upload</button>
      <button class="weui-btn" type="primary" bindtap='downloadFiles'>Download</button>
      <button class="weui-btn" type="warn" bindtap='deleteFiles'>Delete</button>
    </view>

    <!-- 已上传图片 -->
    <view class="weui-cells">
      <view class="text-center">已备份图片</view>
      <view class="weui-cell" wx:for="{{downloadedBackupedFiles}}">
        <image class="" src="{{item}}" mode="aspectFill" data-index="{{index}}" data-type="DownloadedView" bindlongtap="longTapConfirm" />
      </view>
    </view>
    <view class='text-center' wx:if="{{downloadedBackupedFiles.length == 0}}">暂无</view>
  </view>
</view>
```


## 1.2.1 imgbackup.js
- claim app=getApp() to use globalData
- create data list: `needUploadFiles`, `downloadedBackupedFiles`.
- the apis below which is started by `wx.` is the wx origin apis, these apis should be wrapped in a function to use.
- `chooseImage` and `previewImage` function is copied from weui uploader js, other function is created manually.

wx.apis
- [wx.chooseImage(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.chooseImage.html)
- [wx.previewImage(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.previewImage.html)
- [UploadTask wx.uploadFile(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/wx.uploadFile.html), 将本地资源上传到服务器。客户端发起一个 HTTPS POST 请求

```js
const app = getApp()

Page({
  // 页面的初始数据
  data: {
    needUploadFiles: [],
    downloadedBackupedFiles: []
  },

  chooseImage: function (e) {
    var that = this;
    wx.chooseImage({
      sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
      success: function (res) {
        // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
        that.setData({
          needUploadFiles: that.data.needUploadFiles.concat(res.tempFilePaths)
        });
      }
    })
  },

  previewImage: function (e) {
    wx.previewImage({
      current: e.currentTarget.id, // 当前显示图片的http链接, e.currentTarget.dataset.dataId
      urls: this.data.files // 需要预览的图片http链接列表
    })
  },

  uploadFiles: function(){
    for (var i = 0; i < this.data.needUploadFiles.length; i ++){
      var filePath = this.data.needUploadFiles[i]   // 迭代待上传文件列表，每一个都执行上传操作
      wx.uploadFile({
        url: app.globalData.serverUrl + app.globalData.apiVersion + 'service/image/',
        filePath: filePath,
        name: 'test',
        success: function(res){
          console.log(res)
        }
      })
    }
  },

  downloadFiles: function(){

  },

  deleteFiles: function(){

  },
})
```
- when click upload button in imgbackup.wxml, the `bindtap='uploadFiles'` attribute will call the `uploadFiles: function()`
- `uploadFiles: function()` will first get the full file path that select by `chooseImage: function()`
- POST request to django backend, by the file name 'test'
- if success print log
  - pic direction has been rotated?????n

![](https://i.loli.net/2019/06/09/5cfcd005d3cbb26558.png)


# 2. DownloadFiles
## 2.1 imgbackup.js
wx.apis
- [DownloadTask wx.downloadFile(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/network/download/wx.downloadFile.html), 下载文件资源到本地。客户端直接发起一个 HTTPS GET 请求，返回文件的本地临时路径，单次下载允许的最大文件为 50MB。
  - because of download is a GET request, therefore django `ImageView.get()` will handle this request
```js
downloadFiles: function(){
    var that = this
    wx.downloadFile({
      url: app.globalData.serverUrl + app.globalData.apiVersion + 'service/image/' + 
        '?md5=' + 'f45d562179d0e7f0990326e9de2b55cf',
      success: function(res) {
        var tempFile = res.tempFilePath
        var newDownloadedBackupedFiles = that.data.downloadedBackupedFiles
        newDownloadedBackupedFiles.push(tempFile)
        that.setData({
          downloadedBackupedFiles: newDownloadedBackupedFiles
        })
      }
    })
  },
```
- we use a static md5 name for test, in production env, should select specific image and download by its md5
![](https://i.loli.net/2019/06/09/5cfcd8624b35977902.png)

# 3. DeleteFiles
wx.apis does not provide a deleteFile api, we need to wx.request(method='DELETE') to delete the file which is satored in backend server.
## 3.1 django backend
```python
class ImageView(View, response.CommonResponseMixin):
    def get(self, request):
        ...
    def post(self,request):
        ...
        
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
```
## 3.2 wx frontend
wx.apis
- [RequestTask wx.request(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html)
  - why `res.data` in `success: function(res){ console.log(res.data)}` can refer to the api manual. 
  -   object.Success Callback - Object res

    |property|type|description|version|
    |-|-|-|-|
    |data	|string/Object/Arraybuffer	|Data returned by developer server	||
    |statusCode|	number|	HTTP status code returned by developer server||	
    |header|	Object|	HTTP Response Header returned by the developer server|	1.2.0|


```js
deleteFiles: function(){
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion + 'service/image/' +
        '?md5=' + 'f45d562179d0e7f0990326e9de2b55cf', // same url as the download url
      method: 'DELETE',
      success: function(res){
        console.log(res.data)
        wx.showToast({
          title: 'Delete success.',
        })
      }
    })
```
![](https://i.loli.net/2019/06/09/5cfcdd26e05e218156.png)





