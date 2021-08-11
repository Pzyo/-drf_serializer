
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from app03.models import Book
from app03.ser import BookModelSerializer
from rest_framework.response import Response


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