from urllib import response
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import QuestionAnswerSerializer, QuestionSerializer,SubmittedAnswerSerializer
from .models import Question,Options,Answer, SubmittedAnswer


# Create your views here.

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
		'Questions':'/quiz-questions/',
		'Answer submission':'/submit-answers/',
		'Submitted answers':'/submitted-answers/',
        'Answers':'/answers/',
        'Score':'/score/'
		}

    return Response(api_urls)

@api_view(['GET'])
def quizQuestions(request):
    questions=Question.objects.select_related('options').order_by('quesId')
    serializer=QuestionSerializer(instance=questions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def submitAnswers(request):
    
    serializer=SubmittedAnswerSerializer(data=request.data, many=True)

    print(request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def submittedAnswers(request):
    answers=SubmittedAnswer.objects.all()
    serializer=SubmittedAnswerSerializer(instance=answers,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def questionsWithAnswers(request):
    questions=Question.objects.select_related().order_by('quesId')
    serializer=QuestionAnswerSerializer(instance=questions, many=True)
    return Response(serializer.data)

def score(request):
    questions=Question.objects.all()
    score=0
    for question in questions:
        submittedAnswer=question.submission.submittedAnswer
        answer=question.answer.answer

        if answer==submittedAnswer:
            score=score+1

    percentScore=float(score)/float(questions.count())*100.00
    result=''

    if percentScore<50.00:
        result='Fail'
    else:
        result='Pass'
        
          
    return JsonResponse({'questions':questions.count(),
    'score':score,
    'percentage':f'{percentScore:.2f}',
    'result':result
    })