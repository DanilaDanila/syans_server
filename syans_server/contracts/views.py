from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from .models import Contract
from .serializers import ContractSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth.models import User

# from rest_framework_simplejwt.backends import TokenBackend


class ContractsView(APIView):
    def get(self, request, format=None):
        if request.auth is None:
            return Response({}, status.HTTP_403_FORBIDDEN)

        uid = request.user.id
        username = request.user.username
        role = request.user.last_name
        if username == 'admin':
            contracts = Contract.objects.all()
        else:
            if 'id' in request.query_params.keys():
                contracts = [Contract.objects.get(id=request.query_params['id'][0])]
            elif role == 'blogger':
                contracts = Contract.objects.all().filter(executor = uid).order_by('-id')
            else:
                contracts = Contract.objects.all().filter(customer = uid).order_by('-id')
            
        response = ContractSerializer(contracts, many=True)

        return JsonResponse(data=response.data, safe=False)

    def post(self, request, format=None):
        if request.auth is None:
            return Response({}, status.HTTP_403_FORBIDDEN)

        print(request.data)
        data = request.data

        if data['id'] == -1:
            new_contract = Contract(
                title='New contract',
                task='',
                customer=User.objects.all().filter(username=request.user.username)[0],
                executor=User.objects.all().filter(username='superblogger')[0],
                cost=0,
                status='offered'
            )
            new_contract.save()
        else:
            contract = Contract.objects.get(id=data['id'])
            for key in data.keys():
                value = data[key]
                if key == 'title':
                    contract.title = value
                elif key == 'task':
                    contract.task = value
                elif key == 'customer':
                    value = User.objects.all().filter(username=value)[0]
                    contract.customer = value
                elif key == 'executor':
                    value = User.objects.all().filter(username=value)[0]
                    contract.executor = value
                elif key == 'cost':
                    contract.cost = int(value)
                elif key == 'status':
                    contract.status = value
            contract.save()

        return Response({}, status.HTTP_200_OK)
