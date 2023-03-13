from django.shortcuts import render
# import API VIEW
from rest_framework.views import APIView
from .models import Sales
from .serializers import SalesSerializer
from rest_framework.response import Response
import datetime

# get current date
todays_date = datetime.datetime.now().date()

class SalesApiView(APIView):
    def get(self, request):
        # make query basing on current date
        sales = Sales.objects.filter(date=todays_date)
        serializer = SalesSerializer(sales, many=True)
        
        return Response({"sales": serializer.data})
    
    def post(self, request):
        print(request.data)
         
        return Response({"sales": "Post request was made"})
    