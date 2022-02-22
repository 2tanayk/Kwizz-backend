from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('quiz-questions/', views.quizQuestions, name='quiz-questions'),
    path('submit-answers/', views.submitAnswers, name='submit-answers'),
    path('submitted-answers/', views.submittedAnswers, name='submitted-answers'),
    path('answers/', views.questionsWithAnswers, name='answers'),
    path('score/', views.score, name='score'),
]