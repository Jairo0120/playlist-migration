from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TestView(APIView):
    def get(self, request):
        var_test = False
        another_var = 'String random'
        return Response(
            data={'data': 'Hola mundo'},
            status=status.HTTP_200_OK
        )
