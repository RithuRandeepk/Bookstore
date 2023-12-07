from rest_framework import serializers
from api.models import Books,Carts,Reviews
from django.contrib.auth.models import User



class BookSerializers(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    bookname = serializers.CharField()
    author = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    category = serializers.CharField()

class BookModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = "__all__"
        # field=["name","price","description"]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class CartSerializer(serializers.ModelSerializer):

    id = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    product = serializers.CharField(read_only=True)
    date = serializers.CharField(read_only=True)

    class Meta:

        model = Carts
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):

    product = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Reviews
        fields = "__all__"


