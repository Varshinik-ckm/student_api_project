
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

@api_view(['GET'])
def adult_students(request):
    students = Student.objects.filter(age__gt=18)
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)
