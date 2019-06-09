

class ReturnCode:
    # 状态码
    SUCCESS = 0
    FAILED = -100
    RESOURCE_NOT_EXIST = -500
    BROKEN_AUTHORIZED_DATA = -501
    WRONG_PARAMS = -101

    @classmethod
    def message(cls, code):
        # 根据状态码转换成说明文字
        if code == cls.SUCCESS:
            return 'success'
        elif code == cls.FAILED:
            return 'failed'
        elif code == cls.UNAUTHORIZED:
            return 'unauthorized'
        elif code == cls.WRONG_PARAMS:
            return 'wrong_params'
        else:
            return ''


def wrap_json_response(data=None, code=None, message=None):
    # 将一个Jsonresponse，再包装上code和message两个信息
    # return一个dict结构，再有safe=false读取将一个Jsonresponse
    response = {}
    if not code:
        code = ReturnCode.SUCCESS
    if not message:
        message = ReturnCode.message(code)
    if data:
        response['data'] = data
    response['code'] = code
    response['message'] = message
    return response

class CommonResponseMixin(object):
    @classmethod
    def wrap_json_response(cls, data=None, code=None, message=None):
        response = {}
        if not code:
            code = ReturnCode.SUCCESS
        if not message:
            message = ReturnCode.message(code)
        if data:
            response['data'] = data
        response['code'] = code
        response['message'] = message
        return response