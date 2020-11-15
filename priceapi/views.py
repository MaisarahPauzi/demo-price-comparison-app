from django.views.generic import TemplateView
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import requests
from bs4 import BeautifulSoup
import json
from pricedb.models import SearchHistory, RealEstateProperty
import pandas as pd
from django.http import HttpResponse
from django.db.models import F

def download_data(request):
    qs = RealEstateProperty.objects.all().select_related('history').annotate(search_keyword=F('history__title')).values('name', 'link', 'image', 'price', 'search_keyword')
    data_list = list(qs)
    results = pd.DataFrame(data_list)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=all_data.csv'

    results.to_csv(path_or_buf=response)
    return response

def parse_javascript_str(jstr):
    formatted_js = jstr.replace('<script type="application/ld+json">','')
    formatted_js = formatted_js.replace('</script>','')
    json_js=json.loads(formatted_js)
    return json_js[2]['itemListElement']


class ApiEndpoint(APIView):
    @swagger_auto_schema(
        operation_description="Search location", 
        responses={201: 'New Properties Scrapped'}, 
        request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={
            'location': openapi.Schema(type=openapi.TYPE_STRING, description='Location/Area'),
        })
    )
    def post(self, request, format=None):
        location = request.data.get('location')
        BASE_URL = "https://www.mudah.my/malaysia/properties-for-sale-2000?q="
        search_query = location
        URL = BASE_URL + search_query

        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        js = soup.find('script', {"type":"application/ld+json"})
        jstr= str(js)
        items_lists = parse_javascript_str(jstr)

        items = []

        # save in DB
        s = SearchHistory.objects.create(title=search_query)
        
        for item_list in items_lists:
            items.append({'name':item_list['item']['name'], 'link':item_list['item']['url'], 'image':item_list['item']['image'], 'price':item_list['item']['offers']['price']})
            r = RealEstateProperty.objects.create(
                name = item_list['item']['name'],
                link = item_list['item']['url'],
                image = item_list['item']['image'],
                price = item_list['item']['offers']['price'],
                history = s
            )


        context_data = {
            'Source': 'Mudah.my',
            'Results': items
        }
        return Response(context_data, status=status.HTTP_201_CREATED)
    