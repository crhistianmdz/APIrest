from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """API view de prueba"""

    serializer_class = serializers.HelloSerializer
    
    
    def get(self, request,format=None):
        """retornar lista de caracteristicas del APIview"""
        an_apiview=[
            'usamos metodos http como funciones (get, post, patch, put, delete)',
            'es similar a una vista tradicional de django',
            'nos da el amyor control sobre la logica de nuestra aplicacion',
            'esta mapeado manuealmente los urls',
        ]
        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self,request):
        """crear un mensaje con nuestro nombre"""
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self,request,pk=None):
        """maneja actualizar un objeto"""
        return Response({'method':'PUT'})

    def patch(self,reques,pk=None):
        """Maneja actualizacion parcial de un objeto"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """elimina un objeto"""
        return Response({'method':'DELETE'})