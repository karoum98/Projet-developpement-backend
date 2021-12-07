from django.http import HttpResponse
from .service.English_sentiment_analysis import english_sentiment_counter
from .service.French_sentiment_analysis import french_sentiment_counter
from .data.data_tmp import data
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

@csrf_exempt
def analyse_sentimentalAPI(request):
    if request.method == 'GET':
        results = french_sentiment_counter(data)
        return JsonResponse(results, safe=False)


