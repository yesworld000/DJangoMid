from rest_framework import serializers
from api.models import Book, Journal


class BookSerializer(serializers.ModelSerializer):
    description = serializers.CharField()

    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'created_at')


class JournalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        company = Journal.objects.create(name=validated_data.get('publisher'))
        return company

    def update(self, instance, validated_data):
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.save()
        return instance