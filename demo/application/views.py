from django.http import Http404
from django.shortcuts import get_object_or_404, render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join(f"&laquo;{q.question_text}&raquo;" for q in latest_question_list)

    return render(
        request,
        "application/index.html",
        {
            'latest_question_list': latest_question_list
        }
    )


def detail(request, question_id):
    question = Question.objects.filter(pk=question_id).first()
    if question:
        response = render(
            request,
            "application/detail.html",
            {
                "question": question,
            }
        )
    else:
        raise Http404("Вопрос не существует.")

    return response


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(
        request,
        "application/results.html",
        {
            'question': question
        }
    )


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    selected_choice = question.choice_set.filter(pk=request.POST.get('choice')).first()
    if selected_choice:
        selected_choice.votes += 1
        selected_choice.save()
        response = HttpResponseRedirect(
            reverse('application:results', args=(question.id, ))
        )
    else:
        response = render(
            request,
            "application/detail.html",
            {
                'question': question,
                'error_message': 'Вы не выбрали вариант ответа.'
            }
        )

    return response
