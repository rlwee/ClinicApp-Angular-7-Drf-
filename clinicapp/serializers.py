from rest_framework import serializers
from .models import Clients, Schedule, Sales, Employee, Workload
from django.contrib.auth.models import User, Group
from django import forms
from rest_framework.validators import UniqueValidator



class ClientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Clients
        fields = ('id',
                  'name',
                  'age',
                  'address',
                  'mothersName',
                  'fathersName',
                  'contactNumberM',
                  'contactNumberF',
                  'pediaName',
                  'history',
                  'diagnosis',
                  'payment',
                  'therapyType')

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Schedule
        fields = (
                  'id',
                  'client',
                  'present',
                  'ref',
                  'service',
                  'paid',
                  'schedule')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ('date_created',
                  'name',
                  'age',
                  'address',
                  'contact',
                  'SSS',
                  'TIN')

class WorkloadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Workload
        fields = ('date_created',
                  'employee',
                  'tasks')

class SalesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sales
        fields = ('day',
                  'week',
                  'month')