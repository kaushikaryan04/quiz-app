from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
from .models import Question, Option, QuizSession
import shutil



def register_view(request) :
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            user = form.save()
            login(request , user )
            return redirect('main')
        else :
            messages.error(request , "Invalid form")
            return render(request , 'main/register.html',{"form" : form})
    else :
        form = UserCreationForm()
        return render(request , 'main/register.html',{"form" : form})

@login_required
def main(request) :
    if request.method == 'POST' :
        for key, value in request.POST.items():
            if key.startswith("question_"):
                question_id = key.split("_")[1]
                selected_option_id = value
                question = Question.objects.get(id=question_id)
                selected_option = Option.objects.get(id=selected_option_id)

                is_correct = selected_option.is_true

                QuizSession.objects.create(
                    user=request.user,
                    question=question,
                    selected_option=selected_option,
                    is_correct=is_correct,
                )
        return redirect('results')  # Redirect to results page after submission

    all_questions = list(Question.objects.all())
    random.shuffle(all_questions)
    print(all_questions[0:10])
    return render(request, 'main/main.html', {'questions': all_questions[0:10]})

@login_required
def results(request):
    # Calculate and display the results
    sessions = QuizSession.objects.filter(user=request.user)
    total = sessions.count()
    correct = sessions.filter(is_correct=True).count()
    incorrect = total - correct

    return render(request, 'main/scores.html', {
        'total': total,
        'correct': correct,
        'incorrect': incorrect,
        'sessions': sessions,
    })


@login_required
def logout_view(request) :
    logout(request)
    return redirect('login')
