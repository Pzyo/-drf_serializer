from django.conf.urls import url

from app03 import views

# 第一步, 导入routers模块
from rest_framework import routers

# 第二步, 两个类, 实例化得到对象
# routers.DefaultRouter
# routers.SimpleRouter
router_obj = routers.SimpleRouter()
# router_obj = routers.DefaultRouter()
# 第三步, 注册
# 基本格式: router_obj.register('前缀', '继承自ModelViewSet的视图类', '别名') # ps: 前缀无需加斜杠
router_obj.register(r'books4', views.Books4View)
router_obj.register(r'books5', views.Books5View)
# 第四步
# router_obj.urls自动生成的路由
print(router_obj.urls)
"""
SimpleRouter
[
    <RegexURLPattern book-list ^books4/$>, 
    <RegexURLPattern book-detail ^books4/(?P<pk>[^/.]+)/$>
]

DefaultRouter
[
    <RegexURLPattern book-list ^books4/$>, 
    <RegexURLPattern book-list ^books4\.(?P<format>[a-z0-9]+)/?$>, 
    <RegexURLPattern book-detail ^books4/(?P<pk>[^/.]+)/$>, 
    <RegexURLPattern book-detail ^books4/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$>, 
    <RegexURLPattern api-root ^$>, 
    <RegexURLPattern api-root ^\.(?P<format>[a-z0-9]+)/?$>
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

    url(r'^login/$', views.LoginView.as_view()),

    url(r'^test/$', views.TestView.as_view()),
    url(r'^books6/$', views.Book6View.as_view()),
    url(r'^books7/$', views.Book7View.as_view()),

    url(r'^test2/$', views.Test2View.as_view()),

    url(r'^books8/$', views.BookListAPIView.as_view()),
    url(r'^books9/$', views.Books9View.as_view()),

]

# 第五步, 加入urlpatterns
urlpatterns += router_obj.urls