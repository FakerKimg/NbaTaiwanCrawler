from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from news.models import News
from news.serializers import NewsSerializer
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

# Create your views here.
@csrf_exempt
def news_list(request):
    """
    List all news.
    """
    if request.method == 'GET':
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def news_detail(request, href):
    """
    Retrieve a news.
    """
    print(href)
    try:
        news = News.objects.get(href=href[:-1])
    except News.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NewsSerializer(news)
        return JsonResponse(serializer.data)

@csrf_exempt
def news_upload(request):
    """
    Add a new news.
    """
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        data["content"] = "\n".join([k[5:] for k in data["content"] if not k.startswith("img:")])
        data["coverimg"] = ""
        for k in data["content"]:
            if k.startswith("img:"):
                data["coverimg"] = k
                break
        serializer = NewsSerializer(data=data)
        if serializer.is_valid():
            try:
                serializer.save()
                return JsonResponse(serializer.data)
            except IntegrityError:
                pass
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def blank(request):
    return render(request, "blank.html")


