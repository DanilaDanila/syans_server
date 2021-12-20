from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from django.http.response import JsonResponse

class WhoAmI(APIView):
    def get(self, request, format=None):
        print('WHO_AM_I_CALL')
        if request.auth is None:
            return Response({}, status.HTTP_403_FORBIDDEN)

        me = User.objects.get(id=request.user.id)
        return Response({'role': me.last_name}, status.HTTP_200_OK)

class ExecutorsList(APIView):
    def get(self, request, format=None):
        users = User.objects.all().filter(last_name = 'blogger')
        response = UserSerializer(users, many=True)

        return JsonResponse(data=response.data, safe=False)

class Registration(APIView):
    def post(self, request, format=None):
        # login = request.data.login
        # password = request.data.passwd
        # email = request.data.email

        print(request.data)
        new_user = User.objects.create_user(**request.data)
        new_user.save()
        return Response({}, status=status.HTTP_200_OK)