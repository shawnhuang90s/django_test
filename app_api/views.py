from utils.response import APPResponse
from test.global_request_test import global_request_test
from django.utils.translation import gettext as _


def test_global_request(request):
    """测试全局访问请求对象"""
    global_request_test()
    return APPResponse()


def test_multiple_language(request):
    """测试多语言配置是否生效"""
    data = {
        'test': _('this is a test msg.')
    }
    return APPResponse(data=data)
