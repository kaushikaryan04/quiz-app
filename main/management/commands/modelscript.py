from django.core.management.base import BaseCommand
import requests as request
from main.models import Question , Option


class Command(BaseCommand):
    help = 'Generates some questions and options for testing'

    def handle(self , *args ,**kwargs) :
        api_link = 'https://the-trivia-api.com/v2/questions'
        response = request.get(api_link)
        data = response.json()
        questions = []
        for d in data :
            question = d.get('question')['text']
            # first option in the options list is the correct answer
            options = []
            options.append(d.get('correctAnswer'))
            options.extend(d.get('incorrectAnswers'))
            d = {"question" : question , "options"  : options}
            questions.append(d)

        for q in questions :
            question = Question.objects.create(question_text = q['question'])
            for o in q['options']:
                Option.objects.create(question = question , option_text = o , is_true = o == q['options'][0])
