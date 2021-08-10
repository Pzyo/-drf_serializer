from django.shortcuts import render

from rest_framework.views import APIView
from app01.models import Book
from app01.ser import BookSerializer
from rest_framework.response import Response

from app01.utils import MyResponse

class BookView(APIView):
    def get(self, request, pk):
        book = Book.objects.filter(id=pk).first()
        # 实例化
        # 序列化谁, 就把谁传过去
        book_ser = BookSerializer(book)  # 调用类的__init__
        # book_ser.data  序列化对象.data就是序列化后的字典
        return Response(book_ser.data)

    def put(self, request, pk):
        response_msg = {'status':200, 'msg':'成功'}

        book = Book.objects.filter(id=pk).first()
        # 得到序列化类的对象
        book_ser = BookSerializer(instance=book, data=request.data)
        # 数据验证
        if book_ser.is_valid():  # 返回True, 验证通过
            book_ser.save()
            response_msg['data'] = book_ser.data
            return Response(response_msg)
        else:
            response_msg['status'] = 101
            response_msg['msg'] = '数据校验失败'
            response_msg['data'] = book_ser.errors
            return Response(response_msg)

    def delete(self, request, pk):
        response = MyResponse()
        ret = Book.objects.filter(id=pk).first()
        return Response(response.get_dict)

class BooksView(APIView):
    # def get(self, request):
    #     response_msg = {'status': 200, 'msg': '成功'}
    #     books = Book.objects.all()
    #     books_ser = BookSerializer(books, many=True) # 序列化多条, 如果序列化一条无需加many参数
    #     response_msg['data'] = books_ser.data
    #     return Response(response_msg)

    def get(self, request):
        response = MyResponse()

        books = Book.objects.all()
        book = Book.objects.all().first()
        books_ser = BookSerializer(books, many=True)
        book_ser = BookSerializer(book)

        print(type(books_ser))  # <class 'rest_framework.serializers.ListSerializer'>
        print(type(book_ser))   # <class 'app01.ser.BookSerializer'>

        response.data = books_ser.data
        return Response(response.get_dict)

    # 新增
    def post(self, request):
        response_msg = {'status': 200, 'msg': '成功'}
        # 修改时才有instance, 新增没有instance, 只有data
        book_ser = BookSerializer(data=request.data)
        # 校验字段
        if book_ser.is_valid():
            book_ser.save()
            response_msg['data'] = book_ser.data
        else:
            response_msg['status'] = 400
            response_msg['msg'] = '数据校验失败'
            response_msg['data'] = book_ser.errors
        return Response(response_msg)

from app01.ser import BookModelSerializer
class BooksView2(APIView):
    def get(self, request):
        response = MyResponse()
        books = Book.objects.all()
        books_ser = BookModelSerializer(books, many=True) # 序列化多条, 如果序列化一条无需加many参数
        response.data = books_ser.data
        return Response(response.get_dict)