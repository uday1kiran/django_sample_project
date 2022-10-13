from rest_framework import serializers

from demo.models import Book, Character, Author


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','isbn_10', 'isbn_13']

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id','name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','surname']

class BookSerializer(serializers.ModelSerializer):
    ## to display complete object in the API output
    number = BookNumberSerializer(many=False)
    characters = CharacterSerializer(many=True) ## not a column on Book table but linked with related_name in FOreignkey
    authors = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = ['title', 'description', 'price', 'published', 'is_published', 'number','characters','authors']

# class BookMiniSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['id','title']
