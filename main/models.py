from django.db import models
from django.contrib.auth.models import User

class Question(models.Model) :
    question_text = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return str(self.question_text)

class Option(models.Model) :
    question = models.ForeignKey(Question , on_delete= models.CASCADE)
    is_true = models.BooleanField(null = False , blank = True )
    option_text = models.CharField(max_length = 100)


class QuizSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.question_text} - {'Correct' if self.is_correct else 'Incorrect'}"
