
from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField(max_length=16, min_length=3)
    # price = serializers.DecimalField()
    price = serializers.CharField()
    author = serializers.CharField()
    publish = serializers.CharField()

    def validate_price(self, data):  # validate_字段名, 接收一个参数
        # 如果价格小于10, 就校验不通过
        if float(data) > 10:
            return data
        else:
            # 校验失败, 抛出异常
            from rest_framework.exceptions import ValidationError
            raise ValidationError('价格太低')


    def update(self, instance, validated_data):
        # instance是book这个对象
        # validated_data是校验后的数据
        instance.name = validated_data('name')
        instance.price = validated_data('price')
        instance.author = validated_data('author')
        instance.publish = validated_data('publish')
        instance.save()  # book.save()  django的orm提供的
        return instance