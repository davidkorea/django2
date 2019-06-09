# wxapp向django请求图文信息

- 文字信息，请求1次，即可获取所需信息
- 图片信息，请求2次。第一次请求获得资源链接地址，第二期请求根据资源地址获得图片信息

# 1. django后台返货图片信息
- create a PythonPackage named as resources/images to restore images, 2 levels are all PythonPackage. the __init__.py can be deleted.
- create a view to deal with images data
