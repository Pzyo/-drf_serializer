from django.shortcuts import render

from rest_framework.views import APIView
from app01.models import Book
from app01.ser import BookSerializer
from rest_framework.response import Response
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