
from rest_framework.throttling import SimpleRateThrottle


class MyThrottling(SimpleRateThrottle):
    scope = 'luffy'
    def get_cache_key(self, request, view):
        return request.META.get('REMOTE_ADDR')