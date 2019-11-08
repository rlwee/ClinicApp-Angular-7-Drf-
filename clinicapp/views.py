from .serializers import ClientSerializer, ScheduleSerializer, WorkloadSerializer, EmployeeSerializer
from clinicapp.models import Schedule, Clients, Sales, Workload, Employee
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response  import Response



# Create your views here.



class ClientViewSet(viewsets.ViewSet):
    queryset = ''
    serializer_class = ClientSerializer

    def clientList(self, request, **kwargs):
        clients = Clients.objects.all()
        serializer = self.serializer_class(clients, many=True)
        return Response(serializer.data, status=200)

    def createClient(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def clientDetail(self, request, **kwargs):
        client = get_object_or_404(Clients, id=kwargs.get('client_id'))
        serializer = self.serializer_class(client)
        return Response(serializer.data, status=200)

    def clientDelete(self, request, **kwargs):
        client = get_object_or_404(Clients, id=kwargs.get('client_id'))
        client.delete()
        return Response(status=200)

