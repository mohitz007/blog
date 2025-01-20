import json
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from common.authentication import authenticated
from common.serializers import RegisterSerializer
from .models import Author, BlogPost,Token
# Create your views here.


class BlogViewSet(ViewSet):
    def list(self, request):
        # Implement logic to fetch and return blog posts
        try:
            blog_posts = BlogPost.objects.all().select_related("author")
            records = []
            for record in blog_posts:
                data = {
                    "post_id": record.id,
                    "author": record.author.name,
                    "title": record.title,
                    "post": record.content,
                }
                records.append(data)
            return Response(data=records, status=200)
        except Exception as e:
            return Response(data=str(e), status=400)


    @method_decorator(authenticated)
    def create(self, request):
        # Implement logic to create a new blog post
        try:
            blog_post = BlogPost.objects.create(
                title=request.body.get("title"),
                content=request.body.get("content"),
                author_id=request.body.get("user"), # data added from authentication token
            )
            return Response(data={"message": "Blog post created successfully"}, status=201)
        except Exception as e:
            return Response(data=str(e), status=400)
        
    @method_decorator(authenticated)
    def update(self, request,pk=None):
        # Implement logic to update an existing blog post
        try:
            blog_post = BlogPost.objects.get(id=pk)
            if blog_post.author_id != request.body.get("user"):
                return JsonResponse(data={"message": "Unauthorized to update this post"}, status=401)
            blog_post.title = request.body.get("title")
            blog_post.content = request.body.get("content")
            blog_post.save()
            return Response(data={"message": "Blog post updated successfully"}, status=200)
        except Exception as e:
            return Response(data=str(e), status=400)
        
def login(request):
    try:
        # Implement logic to authenticate user and return token
        body = json.loads(request.body)
        username = body.get("username")
        password = body.get("password")
        user = Author.objects.get(username=username)
        if not user:
            return JsonResponse(data={"message": "Invalid username"}, status=400)
        if not user.check_password(password):
            return JsonResponse(data={"message": "Invalid password"}, status=400)
        token = Token.objects.create(user=user)
        return JsonResponse(data={"token": token.token}, status=200)
    except Exception as e:
        return JsonResponse(data={"error":str(e)})

def register(request):
    try:
        # Implement logic to register new user
        body = json.loads(request.body)
        username = body.get("username")
        password = body.get("password")
        name = body.get("name")
        
        
        user = Author.objects.filter(username=username, password=password)
        if user.exists():
            return JsonResponse(data={"message": "User already exists,proceed to login"},status=400)
        
        author = Author(username=username, name=name)
        author.set_password(password)
        author.save()
        return JsonResponse(data={"message": "User registered successfully"}, status=201)
    except Exception as e:
        return JsonResponse(data={"error":str(e)},status=400)