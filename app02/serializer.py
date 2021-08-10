
from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    title123 = serializers.CharField(source='title')
    price = serializers.CharField()
    pub_date = serializers.CharField(source='dateFormat')
    publish = serializers.CharField(source='publish.email')  # 相当于 book.publish.email
    authorsxxx = serializers.SerializerMethodField(source='authors')  # 它需要一个配套方法, 方法名必须是 get_字段名(序列化字段名), 返回值就是要显示的东西

    def get_authorsxxx(self, instance):
        # instance其实是book对象
        authors = instance.authors.all()  # 取出所有作者
        ll = []
        for author in authors:
            ll.append({'name':author.name, 'age':author.age})
        return ll
