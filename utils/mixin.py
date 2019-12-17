class ApiViewMinxin:
    def dispatch(self, request, *args, **kwargs):
        response = super(ApiViewMinxin, self).dispatch(request, *args, **kwargs)
        response = self.get_process_response(request, response, *args, **kwargs)
        return response

    def get_process_response(self, request, response, *args, **kwargs):
        handle = getattr(self, f'process_{self.process_key(request)}', self.get_default_response)
        response = handle(request, response, *args, **kwargs)
        return response

    def process_key(self, request):
        return request.method.lower()

    def get_default_response(self, request, response, *args, **kwargs):
        return response


class ViewSetMixIn(ApiViewMinxin):

    def process_key(self, request):
        return self.action
