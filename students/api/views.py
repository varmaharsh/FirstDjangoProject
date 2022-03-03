from re import sub
from turtle import ht
from django.db.models import Avg, Max
from django.http import Http404
from .models import Mark, Student, Subject
from .serializers import MarkSerializer, StudentSerializer, SubjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        students = Student.objects.filter(name=request.user.username)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SubjectView(APIView):
    def get(self):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MarkView(APIView):
    def get(self):
        marks = Mark.objects.all()
        serializer = MarkSerializer(marks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PerformanceView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        students = Student.objects.filter(name=request.user.username)
        if students.count() == 0:
            return Response(status=Http404)
        marks = Mark.objects.filter(student=students[0].id)
        serializer = MarkSerializer(marks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class OverallHighestScorer(APIView):
    def get(self):
        marks = Mark.objects.values('student').annotate(total = Avg('marks')).order_by('total',).first()
        if marks.count() == 0:
            return Response(status=Http404)
        student = Student.objects.filter(id=marks[0].student)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

class IndividualHighestScorer(APIView):
    def get(self, code):
        subject = Subject.objects.filter(code=code)
        if subject.count() == 0:
            return Response(status=Http404)
        marks = Mark.objects.filter(subjects=subject[0].id).order_by('marks').first()
        student = Student.objects.filter(id=marks[0].id)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
