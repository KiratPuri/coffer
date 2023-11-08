from django.shortcuts import render
from dashboard.models import data
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
import json

#Create your views here.

def home(request):
        dict = data.objects.order_by("pk")
        queryset = data.objects.all().values()
        df = pd.DataFrame(queryset, columns=[ "id", "end_year","intensity", "sector", "topic", "insight", "url", "region", "start_year", "impact", "added", "published", "country", "relevance", "pestle", "source", "title", "likelihood"])
        unique_ =  {
        "unique_values": {
        "end_year" : sorted(list(filter(None, df.end_year.unique()))),
        "sector":  sorted(list(filter(None,  df.sector.unique()))),
        "topic":  sorted(list(filter(None,  df.topic.unique()))),
        "region":  sorted(list(filter(None,  df.region.unique()))),
        "country":  sorted(list(filter(None,  df.country.unique()))),
        "source":  sorted(list(filter(None,  df.source.unique())))
        }
        }
        return render(request, "dashboard.html", context=unique_)

class chart_data (APIView):

    authentication_classes = []
    permission_classes = []

    # def post(self, request, format=None):

    #     authorization_header = request.META.get('HTTP_AUTHORIZATION')  # Example: Authorization header
    #     content_type_header = request.META.get('CONTENT_TYPE')  # Example: Content-Type header

    #     # Accessing POST payload
    #     if request.method == 'POST':
    #         post_data = request.POST  # Form data in case of form submission
    #         raw_post_data = request.body  # Raw body data

    #         # For JSON data in the body (if sent as application/json)
    #         if 'application/json' in content_type_header:
    #             import json
    #             json_data = json.loads(raw_post_data)
    #             print(json_data)
    #             # dict = data.objects.order_by("pk")
    #             # queryset = data.objects.all().values()
    #             # df = pd.DataFrame(queryset, columns=[ "id", "end_year","intensity", "sector", "topic", "insight", "url", "region", "start_year", "impact", "added", "published", "country", "relevance", "pestle", "source", "title", "likelihood"])
    #             # json12 = df.to_json(orient = "records") 

    #             # Handle the data or return a response
    #             return JsonResponse({'message': 'Success'})
    #     else:
    #         return JsonResponse({'error': 'Invalid request method'})

    def get(self, request, format=None):
        #Read query param
        parameters = request.GET.dict()
        #print(type(parameters))
        if(len(parameters) == 2 and parameters['filterType'] is not None and parameters['filterValue'] is not None):
            filterType = parameters['filterType']
            filterValue = parameters['filterValue']
            kwargs = {'{0}'.format(filterType): '{0}'.format(filterValue),}
            #dict = data.objects.filter(**kwargs).order_by("pk")
            queryset = data.objects.filter(**kwargs).order_by("pk").values()
        else:
            queryset = data.objects.all().order_by("pk").values()
        
        #df = pd.DataFrame(queryset, columns=[ "id", "end_year","intensity", "sector", "topic", "insight", "url", "region", "start_year", "impact", "added", "published", "country", "relevance", "pestle", "source", "title", "likelihood"])

        return JsonResponse(list(queryset), safe=False) #JsonResponse(df.to_json(orient='records'))


class filters(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format = None):
        dict = data.objects.order_by("pk")
        queryset = data.objects.all().values()
        df = pd.DataFrame(queryset, columns=[ "id", "end_year","intensity", "sector", "topic", "insight", "url", "region", "start_year", "impact", "added", "published", "country", "relevance", "pestle", "source", "title", "likelihood"])
        unique_values = {
        "end_year" : sorted(list(filter(None, df.end_year.unique()))),
        "sector":  sorted(list(filter(None,  df.sector.unique()))),
        "topic":  sorted(list(filter(None,  df.topic.unique()))),
        "region":  sorted(list(filter(None,  df.region.unique()))),
        "country":  sorted(list(filter(None,  df.country.unique()))),
        "source":  sorted(list(filter(None,  df.source.unique())))
        }
        # pprint(respObj)
        # unique_values=json.dumps(unique_values)
        # data1 = json.loads(str(respObj))
        # json_data = json.dumps(unique_values)
        # jsonstr1 = json.dumps(respObj)        
        # output = json.loads(str(respObj))
        return JsonResponse(unique_values, safe=False)