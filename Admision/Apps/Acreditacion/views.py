from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# 
from .models import *
from .serializers import *



@api_view(['POST','GET'])
def acreditacion_api_GP(request):
    if request.method == 'POST':
        return Response({'message': 'POST'})

    if request.method == 'GET':
        return Response({'message': 'GET'})



@api_view(['PUT','GET','DELETE'])
def acreditacion_api_PGD(request,pk):
    print(type(pk))
    try:
        acreiditacion_data = Acreditacion.objects.filter(id=int(pk)).first()
        # acreiditacion_data = Acreditacion.objects.get(pk)
    except Acreditacion.DoesNotExist:
        return Response({'message': 'No hay datos'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response({'message': f'''GET - PARAMETER {pk}'''})
    
    if request.method == 'PUT':
        return Response({'message': f'''PUT - PARAMETER {pk}''' })
    
    if request.method == 'DELETE':
        return Response({'message': f'''DELETE - PARAMETER {pk}'''})