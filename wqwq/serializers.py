from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tovar
from .serializers import TovarSerializer

class TovarAPI(APIView):     
    def get(self, request):
        malumot = Tovar.objects.all() 
        serializer = TovarSerializer(malumot, many=True)
        return Response(serializer.data)

    def post(self, request):
        kop_narsami = isinstance(request.data, list)
        serializer = TovarSerializer(data=request.data, many=kop_narsami)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)