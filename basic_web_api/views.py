from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# #  ================ WITHOUT DECORATORS ==================
# # Create your views here.

# # a view to list all articles
# @csrf_exempt # included this line to be able to post data from postman. otherwise, for security reasons it should not be so. 
# def article_list (request):

#     if request.method ==  'GET':
#         # fetch all articles from the db
#         articles = Article.objects.all()
#         # serialize. We add many=true because this is a query set, we are fetching more than one article.
#         serializer = ArticleSerializer(articles, many=True)
#         # return a json response
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)

#         # check whether data is valid
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)

#     except Article.DoesNotExist:
#         return HttpResponse(status = 404)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)

#         # check whether data is valid
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)


# ==============WITH DECORATORS=================
#  ================ WITHOUT DECORATORS ==================
# Create your views here.

# a view to list all articles
@api_view(['GET', 'POST'])
def article_list (request):

    if request.method ==  'GET':
        # fetch all articles from the db
        articles = Article.objects.all()
        # serialize. We add many=true because this is a query set, we are fetching more than one article.
        serializer = ArticleSerializer(articles, many=True)
        # return a json response
        return Response(serializer.data)

    elif request.method == 'POST':
        
        serializer = ArticleSerializer(data = request.data)

        # check whether data is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)

        # check whether data is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

