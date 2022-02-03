from django.http import HttpResponse
from .service.English_sentiment_analysis import english_sentiment_counter
from .service.French_sentiment_analysis import french_sentiment_counter

from .data.data_tmp import data_facebook_tmp
from .data.data_facebook import data_from_facebook

from apify_client import ApifyClient
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

@csrf_exempt
def analyse_sentimentalAPI(request):
    if request.method == 'POST':
        param_request = JSONParser().parse(request)
        #data = data_facebook_tmp(param_request["filiales"], param_request["dateDebut"])
        data = data_from_facebook(param_request["filiales"] , param_request["dateDebut"])
        results = {}
        for filiale in data :
            results[filiale] = french_sentiment_counter(data[filiale])
        return JsonResponse(results, safe=False)


