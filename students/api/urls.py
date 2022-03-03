from django.urls import path

from .views import StudentView, SubjectView, MarkView, PerformanceView, OverallHighestScorer

urlpatterns = [
    path('students/', StudentView.as_view()),
    path('subjects/', SubjectView.as_view()),
    path('marks/', MarkView.as_view()),
    path('performance/', PerformanceView.as_view()),
    path('overallHighestScore/<str:code>', OverallHighestScorer.as_view())
]