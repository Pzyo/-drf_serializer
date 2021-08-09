
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from app01.models import Book

# 自定义函数
def check_author_name(data):
    if data.startswith('sb'):
        raise ValidationError('作者名字不能以sb开头')
    else:
        return data

class BookSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=16, min_length=3)
    # price = serializers.DecimalField()
    price = serializers.CharField(write_only=True, required=True)
    author = serializers.CharField(validators=[check_author_name])
    publish = serializers.CharField()

    # 局部钩子
    def validate_price(self, data):  # validate_字段名, 接收一个参数
        # 如果价格小于10, 就校验不通过
        if float(data) > 10:
            return data
        else:
            # 校验失败, 抛出异常
            raise ValidationError('价格太低')

    # 全局钩子
    def validate(self, validate_data):
        print(validate_data)
        author = validate_data.get('author')
        publish = validate_data.get('publish')
        if author == publish:
            raise ValidationError('作者名字与出版社一致')
        else:
            return validate_data

    def update(self, instance, validated_data):
        # instance是book这个对象
        # validated_data是校验后的数据
        instance.name = validated_data('name')
        instance.price = validated_data('price')
        instance.author = validated_data('author')
        instance.publish = validated_data('publish')
        instance.save()  # book.save()  django的orm提供的
        return instance

    def create(self, validated_data):

        # Book.objects.create(
        #     name=validated_data.get('name'),
        #     price=validated_data('price'),
        #     author=validated_data('author'),
        #     publish=validated_data('publish')
        # )

        instance = Book.objects.create(**validated_data)
        return instance


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # 对应上models中的Book表模型
        fields = '__all__'  # 表示序列化所有字段