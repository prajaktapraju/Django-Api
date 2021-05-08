from django.shortcuts import render
from . models import Student
from . serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from . import customauth
# Create your views here.


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [customauth]
    permission_classes = [IsAuthenticated]
