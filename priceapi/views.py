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

class ApiEndpoint(APIView):
    @swagger_auto_schema(
        operation_description="Search product", 
        responses={201: 'New Product Scrapped'}, 
        request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={
            'product': openapi.Schema(type=openapi.TYPE_STRING, description='Product Name'),
        })
    )
    def post(self, request, format=None):
        product = request.data.get('product')
        BASE_URL = "https://www.mudah.my/penang/properties-for-sale-2000?q="
        search_query = product
        URL = BASE_URL + search_query

        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        js = soup.find('script', {"type":"application/ld+json"})
        jstr= str(js)
        formatted_js = jstr.replace('<script type="application/ld+json">','')
        formatted_js = formatted_js.replace('</script>','')
        json_js=json.loads(formatted_js)

        items_lists = json_js[2]['itemListElement']

        items = []

        for item_list in items_lists:
            items.append({'name':item_list['item']['name'], 'link':item_list['item']['url'], 'image':item_list['item']['image'], 'price':item_list['item']['offers']['price']})

        context_data = {
            'Source': 'Mudah.my',
            'Results': items
        }
        return Response(context_data, status=status.HTTP_201_CREATED)
    