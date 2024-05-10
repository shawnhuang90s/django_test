from utils.response import APPResponse
from test.global_request_test import global_request_test


def test_global_request(request):
    """测试全局访问请求对象"""
    global_request_test()
    return APPResponse()
