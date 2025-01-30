from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Turserializer
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from .models import TurModel

# Create your views here.
class TurmodelListCreate(APIView):
    def get(self, request):
        turmodels = TurModel.objects.all()
        serializer = Turserializer(turmodels, many=True)
        return Response(serializer.data)
    
class TurAdminView(APIView):
    permission_classes = [IsAdminUser, ]

    def post(self, request):
        serializer = Turserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TurAdminPK(APIView):
    permission_classes = [IsAdminUser, ]
    def patch(self, request, pk):
        try:
            instance = TurModel.objects.get(pk=pk)
        except TurModel.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = Turserializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            instance = TurModel.objects.get(pk=pk)
        except TurModel.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        instance.delete() 
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

