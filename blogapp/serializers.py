from rest_framework import serializers
from django.contrib.auth import get_user_model #This is best way
from .models import Blog

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", 'email', 'username', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password' : {'write_only': True} #Is can't be seen
        }
    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        password = validated_data['password']
        
        user = get_user_model()
        new_user = user.objects.create(email=email, username=username, 
                                       first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return new_user
    
class SimpleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name']  # Include any other fields you want to expose
    
class BlogSerializer(serializers.ModelSerializer):
    #serializer Inhetance
    author = SimpleAuthorSerializer(read_only=True)  # Use the simple serializer for author
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'author', 'category', 'content', 'featured_image', 'published_date', 'created_at', 'updated_at', 'is_draft']