from django.shortcuts import render
from rest_framework import viewsets, serializers
from django.http import HttpResponse, JsonResponse
from .models import Appointment, Billing,Doctor
from .serializers import AppointmentSerializer,DoctorSerializer,BillingSerializer

class Doctor_data(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class =DoctorSerializer

class AppointmentData(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class BillingData(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
