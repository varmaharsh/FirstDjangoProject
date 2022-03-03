from dataclasses import field
from rest_framework import serializers
from .models import Student, Subject, Mark


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'contact', 'age', 'email' ,'father', 'city']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'code', 'name', 'description', 'instructor']

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ['subject', 'marks']
