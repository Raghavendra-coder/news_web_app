from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .news import get_latest_news
from django.shortcuts import render
import pycountry
from .tasks import add
from celery.result import AsyncResult
# Create your views here.


@api_view(['GET'])
def GetLatestNewsAPI(request):
    try:
        country = request.query_params.get('country')
        language = request.query_params.get('language')
        domain = request.query_params.get('domain')
        news = get_latest_news(country, language, domain)
        data = {
            'success': True,
            'data': news
        }
    except Exception as e:
        data = {
            'success': False,
            'data': e
        }
    return Response(data)

def t_view(request):
    language = request.GET.get('language')
    country = request.GET.get('country')
    domain = request.GET.get('domain')
    data = get_latest_news(country, language, domain)
    languages = {lang.alpha_2: lang.name for lang in pycountry.languages if hasattr(lang, "alpha_2")}
    languages = dict(sorted(languages.items(), key=lambda key: key[1]))

    context = {
        "data": data,
        "domain": ["nytimes", "bbc"],
        "countries": {country.alpha_2: country.name for country in pycountry.countries},
        "languages": languages,
    }

    return render(request, "index.html", context=context)

def automated_call(request):
    language = request.GET.get('language')
    country = request.GET.get('country')
    domain = request.GET.get('domain')
    data = get_latest_news(country, language, domain)
    context = {
        "data": data,
    }
    html = render_to_string("news-feed.html", context)
    data = {
        "html": html
    }
    return JsonResponse(data)


@api_view(['POST'])
def sample(request):
    data = request.data
    a = data["a"]
    b = data["b"]
    result = add.delay(a, b)
    data = {
        "success": True,
        "sum": result.id
    }
    return Response(data)


@api_view(['GET'])
def get_task_status(request, task_id):
    result = AsyncResult(task_id)  # Fetch the result using task_id

    return Response({
        "task_id": task_id,
        "status": result.status,
        "result": result.result if result.ready() else None  # Return result only if completed
    })
