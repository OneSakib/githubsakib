from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import permissions


# Create your views here.
class Index(View):
    def get(self, request):
        print(StudentSerializer)
        return render(request, 'Rest/index.html')


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
