from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers

from .models import Question,Options,Answer, SubmittedAnswer

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Options
        fields=['optionA','optionB','optionC','optionD']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields=['answer']

class QuestionSerializer(serializers.ModelSerializer):
    options=OptionsSerializer(read_only=True)
    
    class Meta:
        model=Question
        fields=['quesId','question','options']

class QuestionAnswerSerializer(serializers.ModelSerializer):
    options=OptionsSerializer(read_only=True)
    answer=AnswerSerializer(read_only=True)
    
    class Meta:
        model=Question
        fields=['quesId','question','options','answer']

class SubmittedAnswerSerializer(serializers.ModelSerializer):
    question=QuestionSerializer(read_only=False)
    class Meta:
        model=SubmittedAnswer
        fields=['question','submittedAnswer','question']

    def create(self, validated_data):
        print('validated data',validated_data)
        question_data = validated_data.pop('question')
        # question=Question.objects.create(quesId=question_data['quesId'],question=question_data['question'])
        question=Question.objects.get(quesId=question_data['quesId'])
        try:
            submission=SubmittedAnswer.objects.get(question=question)
            setattr(submission,'submittedAnswer',validated_data['submittedAnswer'])
            submission.save()
        except SubmittedAnswer.DoesNotExist:
            submission = SubmittedAnswer.objects.create(question=question,submittedAnswer=validated_data['submittedAnswer'])
        return submission

