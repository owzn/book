from django.utils.deprecation import MiddlewareMixin


# 自定义中间件
class TestMiddleware(MiddlewareMixin):
    """中间件，处理请求和响应"""

    def process_request(self, request):
        """处理请求"""
        print("每次请求都会执行的中间件")

    def process_response(self, request, response):
        """处理响应"""
        print("每次响应都会执行的中间件")
        return response
