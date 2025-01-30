from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Turserializer
from rest_framework import status
from .models import TurModel

# Create your views here.
class TurmodelListCreate(APIView):
    def get(self, request):
        turmodels = TurModel.objects.all()
        serializer = Turserializer(turmodels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Turserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
