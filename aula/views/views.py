from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Estudiante

@api_view(['POST'])
@csrf_exempt
def login(request):
    estema = request.data.get('estema')
    estcon = request.data.get('estcon')
    
    try:
        estudiante = Estudiante.objects.get(estema=estema)
        if estudiante.estcon == estcon:
            return Response({'message': 'Se '})
        else:
            return Response({'message': 'Invalid credentials'}, status=400)
    except Estudiante.DoesNotExist:
        return Response({'message': 'Usernot found'}, status=400)