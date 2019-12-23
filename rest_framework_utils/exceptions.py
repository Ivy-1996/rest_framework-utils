from rest_framework.exceptions import APIException


class OssOssStroageSaveFailError(Exception):
    pass


class NotAuthenticatedException(APIException):
    status_code = 401
    default_detail = '登录信息已失效'
    default_code = 'not_authenticated'


class AuthForbiddenException(APIException):
    status_code = 403
    default_code = 'not_authenticated'
    default_detail = '403 Forbidden'
