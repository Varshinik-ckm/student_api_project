
from django.urls import path
from .views import StudentListCreateAPIView, adult_students

urlpatterns = [
    path('', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('adults/', adult_students, name='adult-students'),
]
