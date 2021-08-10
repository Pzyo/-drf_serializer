from django.conf.urls import url

from app03 import views

urlpatterns = [
    url(r'^books/$', views.BooksView.as_view()),
    url(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view()),

    # 使用ModelViewSet编写那5个接口
    url(r'^books2/$', views.Books2View.as_view(actions={'get': 'list', 'post': 'create'})),  # 路径匹配上, 执行get方法, 对应Books2View.list
    url(r'^books2/(?P<pk>\d+)$', views.Books2View.as_view(actions={'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # ViewSetMixin
    url(r'^books3/$', views.Book3View.as_view(actions={'get': 'get_all_book'})),
]