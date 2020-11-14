from django.views.generic import TemplateView
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


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
        context_data = {
            'product': product
        }
        return Response(context_data, status=status.HTTP_201_CREATED)
    