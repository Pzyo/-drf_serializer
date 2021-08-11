from django.conf.urls import url

from app03 import views

# 第一步, 导入routers模块
from rest_framework import routers

# 第二步, 两个类, 实例化得到对象
# routers.DefaultRouter
# routers.SimpleRouter
# router_obj = routers.SimpleRouter()
router_obj = routers.DefaultRouter()
# 第三步, 注册
# 基本格式: router_obj.register('前缀', '继承自ModelViewSet的视图类', '别名') # ps: 前缀无需加斜杠
router_obj.register(r'books4', views.Books4View)
# 第四步
# router_obj.urls自动生成的路由
print(router_obj.urls)
"""
[
    <RegexURLPattern book-list ^books4/$>, 
    <RegexURLPattern book-detail ^books4/(?P<pk>[^/.]+)/$>
]
"""

urlpatterns = [
    url(r'^books/$', views.BooksView.as_view()),
    url(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view()),

    # 使用ModelViewSet编写那5个接口
    url(r'^books2/$', views.Books2View.as_view(actions={'get': 'list', 'post': 'create'})),  # 路径匹配上, 执行get方法, 对应Books2View.list
    url(r'^books2/(?P<pk>\d+)$', views.Books2View.as_view(actions={'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # ViewSetMixin
    url(r'^books3/$', views.Book3View.as_view(actions={'get': 'get_all_book'})),

    # url(r'^books4/$', views.Books4View.as_view(actions={'get': 'list'})),
]

# 第五步, 加入urlpatterns
urlpatterns += router_obj.urls