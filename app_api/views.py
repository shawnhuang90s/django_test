from django.utils.translation import gettext as _

from utils.response import APPResponse
from test.global_request_test import global_request_test
from utils.decorator import track_performance


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


@track_performance(threshold=100)
def test_api_performance(request):
    """测试接口耗时装饰器"""
    for i in range(1000000):
        print(i)
    return APPResponse()
