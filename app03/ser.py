
from rest_framework import serializers
from app03.models import Book
class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'price': {
                'help_text': '价格'
            }
        }