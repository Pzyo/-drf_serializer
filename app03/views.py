
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from app03.models import Book
from app03.ser import BookModelSerializer
from rest_framework.response import Response
from rest_framework.request import Request


# 基于APIView写的
# class BooksView(APIView):
#     def get(self, request):
#         book_list = Book.objects.all()
#         book_ser = BookModelSerializer(book_list, many=True)
#         return Response(book_ser.data)
#
#     def post(self, request):
#         book_ser = BookModelSerializer(data=request.data)
#         if book_ser.is_valid():
#             book_ser.save()
#             return Response({'status': 200, 'msg': 'ok', 'data': book_ser.data})
#         else:
#             return Response({'status':101, 'msg':'校验失败'})
#
# class BookDetailView(APIView):
#     def get(self, request, pk):
#         book = Book.objects.filter(id=pk).first()
#         book_ser = BookModelSerializer(book)
#         return Response(book_ser.data)
#
#     def put(self, request, pk):
#         book = Book.objects.filter(id=pk).first()
#         book_ser = BookModelSerializer(instance=book, data=request.data)
#         if book_ser.is_valid():
#             book_ser.save()
#             return Response({'status': 200, 'msg': 'ok', 'data': book_ser.data})
#         else:
#             return Response({'status':101, 'msg':'校验失败'})
#
#     def delete(self, request, pk):
#         Book.objects.filter(id=pk).delete()
#         return Response({'status': 100, 'msg': '删除成功'})

# 基于GenericAPIView写的
# class BooksView(GenericAPIView):
#     # queryset要传queryset对象, 即查询的对象
#     # queryset = Book.objects.all()
#     queryset = Book.objects  # 解决源码发现, 如果传入Book.objects发现不是quertset对象, 会自动加 .all()
#
#     # serializer_class指定使用哪个序列化类来序列化数据
#     serializer_class = BookModelSerializer
#
#     def get(self, request):
#         book_list = self.get_queryset()
#         book_ser = self.get_serializer(book_list, many=True)
#         return Response(book_ser.data)
#
#     def post(self, request):
#         book_ser = self.get_serializer(data=request.data)
#         if book_ser.is_valid():
#             book_ser.save()
#             return Response({'status': 200, 'msg': 'ok', 'data': book_ser.data})
#         else:
#             return Response({'status':101, 'msg':'校验失败'})

# class BookDetailView(GenericAPIView):
#     queryset = Book.objects
#     serializer_class = BookModelSerializer
#
#     def get(self, request, pk):
#         book = self.get_object()
#         book_ser = self.get_serializer(book)
#         return Response(book_ser.data)
#
#     def put(self, request, pk):
#         book = self.get_object()
#         book_ser = self.get_serializer(instance=book, data=request.data)
#         if book_ser.is_valid():
#             book_ser.save()
#             return Response({'status': 200, 'msg': 'ok', 'data': book_ser.data})
#         else:
#             return Response({'status':101, 'msg':'校验失败'})
#
#     def delete(self, request, pk):
#         self.get_object().delete()
#         return Response({'status': 100, 'msg': '删除成功'})

from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
# class BooksView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     # queryset要传queryset对象, 即查询的对象
#     # queryset = Book.objects.all()
#     queryset = Book.objects  # 解决源码发现, 如果传入Book.objects发现不是quertset对象, 会自动加 .all()
#
#     # serializer_class指定使用哪个序列化类来序列化数据
#     serializer_class = BookModelSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
# class BookDetailView(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
#     queryset = Book.objects
#     serializer_class = BookModelSerializer
#
#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#
#     def put(self, request, pk):
#         return self.update(request, pk)
#
#     def delete(self, request, pk):
#         return self.destroy(request, pk)

from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView

# class BooksView(ListAPIView, CreateAPIView):
class BooksView(ListCreateAPIView):
    queryset = Book.objects
    serializer_class = BookModelSerializer


# class BookDetailView(UpdateAPIView, RetrieveAPIView, DestroyAPIView):
class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects
    serializer_class = BookModelSerializer


from rest_framework.viewsets import ModelViewSet
class Books2View(ModelViewSet):
    queryset = Book.objects
    serializer_class = BookModelSerializer

from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet, GenericViewSet

from rest_framework.viewsets import ViewSetMixin
class Book3View(ViewSetMixin, APIView):  # ViewSetMixin一定要放在APIView前面
    def get_all_book(self, request):
        book_list = Book.objects.all()
        book_ser = BookModelSerializer(book_list, many=True)
        return Response(book_ser.data)

class Books4View(ModelViewSet):
    queryset = Book.objects
    serializer_class = BookModelSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().all()[:3])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

from rest_framework.decorators import action

from rest_framework.authentication import BaseAuthentication

# class Books5View(ModelViewSet):
#     queryset = Book.objects
#     serializer_class = BookModelSerializer
#
#     # action是装饰器, 第一个参数methods传一个列表, 存放请求方式
#     # 第二个参数detail传布尔类型,
#     # 如果detail是False: ^app03/ ^books5/get_2/$ [name='book-get-2']  # 向该地址发送get请求, 会执行下面的函数
#     # 如果detail是True: ^app03/ ^books5/(?P<pk>[^/.]+)/get_2/$ [name='book-get-2']
#     @action(methods=['get'], detail=True)
#     def get_2(self, request):
#         book = self.get_queryset().all()[:2]
#         ser = self.get_serializer(book, many=True)
#         return Response(ser.data)

from app03 import models
import uuid
class LoginView(APIView):
    authentication_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = models.User.objects.filter(username=username, password=password).first()
        if user:
            # 登录成功, 生成随机字符串
            token = uuid.uuid4()
            # 存到Usertoken表中
            # models.UserToken.objects.create(token=token, user=user)  # 每次登录都会记录一次, 效果不好, 应该是更新原token
            # update_or_create有就更新, 没有就新增
            models.UserToken.objects.update_or_create(defaults={'token':token}, user=user)
            return Response({'status':100, 'msg':'登录成功', 'token':token})
        else:
            return Response({'status': 101, 'msg': '用户名或密码错误'})

from app03.app_auth import MyAuthentication, UserPermisson
class Books5View(ModelViewSet):
    queryset = Book.objects
    serializer_class = BookModelSerializer
    # 先用认证类
    authentication_classes = [MyAuthentication]
    # 再用权限类
    permission_classes = [UserPermisson]

    @action(methods=['get'], detail=True)
    def get_2(self, request):
        book = self.get_queryset().all()[:2]
        ser = self.get_serializer(book, many=True)
        return Response(ser.data)

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.throttling import AnonRateThrottle
class TestView(APIView):
    # 说明, 一旦使用内置权限, 最好认证类、权限类都是使用rest框架内置的, 建议不要混着用
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
    throttle_classes = [AnonRateThrottle]

    def get(self, request):
        return Response('测试, 超级用户可以看')

# 过滤组件
from rest_framework.generics import ListAPIView
from app03.models import Book
from app03.ser import BookModelSerializer
class Book6View(ListAPIView):
    queryset = Book.objects
    serializer_class = BookModelSerializer
    filter_fields = ['name','price']

# 排序组件
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
class Book7View(ListAPIView):
    queryset = Book.objects
    serializer_class = BookModelSerializer
    # 先过滤, 再排序
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['name','price']
    # 按照id跟价格排序
    ordering_fields = ['id', 'price']

# 全局异常处理
# drf的异常处理, 默认处理404以及权限等问题, 其他交回给django处理
from rest_framework.views import exception_handler

# 自定义异常处理
from rest_framework import status
def my_exception_handler(exc, context):
    response=exception_handler(exc, context)
    # 两种情况, 一个是None, drf没有处理
    # response对象, drf处理, 但是处理的不合符要求

    if not response:
        # 更细致的捕获异常
        if isinstance(exc, ZeroDivisionError):
            return Response(data={'status': 777, 'msg': str(exc)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data={'status':999, 'msg':str(exc)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # return response
        return Response(data={'status':888, 'msg':response.data.get('detail')}, status=status.HTTP_400_BAD_REQUEST)


from utils.apiresponse import APIResponse
class Test2View(APIView):
    def get(self, request):
        return APIResponse(data={'name':'pzyo'}, token='abcdefg')