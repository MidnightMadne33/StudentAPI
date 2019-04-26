from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics


class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
