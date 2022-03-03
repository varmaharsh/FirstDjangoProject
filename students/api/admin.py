from django.contrib import admin
from api.models import Student, Subject, Mark

# Register your models here.

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Mark)