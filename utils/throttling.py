
from rest_framework.throttling import SimpleRateThrottle


class MyThrottling(SimpleRateThrottle):
    scope = 'luffy'
    def get_cache_key(self, request, view):
        return request.META.get('REMOTE_ADDR')



import time
from rest_framework.throttling import BaseThrottle
# 可以不继承BaseThrottle, 但是必须重写allow_request和wait, 形成鸭子类型
class IPThrottle(object):
    VISIT_DIC = {}
    def __init__(self):
        self.histroy_list = []

    def allow_request(self, request, view):
        '''
        流程:
        1. 取出访问者IP
        2. 判断当前IP不在访问字典里, 添加进去, 并且直接返回True, 表示第一次访问, 在字典里则继续往下走
        3. 循环判断当前IP的列表, 有值, 并且当前时间减去列表的最后一个时间大于60s, 把这种数据pop掉, 这样列表中只有60s内的访问时间
        4. 判断, 当列表小于3, 说明一分钟以内访问不足三次, 把当前时间插入到列表第一个位置, 返回True, 顺利通过
        5. 当大于等于3, 说明一分钟内访问超过三次, 返回False验证失败
        '''
        ip = request.META.get('REMOTE_ADDR')
        ctime = time.time()

        if ip not in self.VISIT_DIC:
            self.VISIT_DIC[ip] = [ctime,]
            return True
        self.histroy_list:list = self.VISIT_DIC[ip]  # 取出当前访问者时间列表
        while True:
            if ctime - self.histroy_list[-1] > 60:
                self.histroy_list.pop()
            else:
                break
        if len(self.histroy_list) < 3:
            self.histroy_list.insert(0, ctime)
            return True
        else:
            return False

    def wait(self):
        # 60 - (当前时间 - 减去列表中最后一个时间)
        ctime = time.time()
        return 60 - (ctime - self.histroy_list[-1])