from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """API view de prueba"""
    def get(self, request,format=None):
        """retornar lista de caracteristicas del APIview"""
        an_apiview=[
            'usamos metodos http como funciones (get, post, patch, put, delete)',
            'es similar a una vista tradicional de django',
            'nos da el amyor control sobre la logica de nuestra aplicacion',
            'esta mapeado manuealmente los urls',
        ]
        return Response({'message':'hello','an_apiview':an_apiview})