from rest_framework.utils.serializer_helpers import ReturnDict

ALL_FIELDS = '__all__'


class ApiViewMinxin:
    def dispatch(self, request, *args, **kwargs):
        response = super(ApiViewMinxin, self).dispatch(request, *args, **kwargs)
        response = self.get_process_response(request, response, *args, **kwargs)
        return response

    def get_process_response(self, request, response, *args, **kwargs):
        # 如果想自定义单独方式的返回对象,自定义`process_{self.process_key(request)}`
        handle = getattr(self, f'process_{self.process_key(request)}', self.get_default_response)
        response = handle(request, response, *args, **kwargs)
        return response

    def process_key(self, request):
        # 设置关键字参数
        return request.method.lower()

    def get_default_response(self, request, response, *args, **kwargs):
        # 通用的请求处理,默认返回原始的数据,如果要diy,请重写该方法
        return response


class ViewSetMixIn(ApiViewMinxin):

    def process_key(self, request):
        # 将关键字转换为`action`
        return self.action


class SerializerMixIn:

    @property
    def data(self):
        # 可在在Meta属性里面定义data对象,该对象支付覆盖原始的data,用于自定义返回应答
        result = getattr(self.Meta, 'data', None)
        response = ReturnDict(result, serializer=self) if result else super(SerializerMixIn, self).data()
        return response

