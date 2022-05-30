from django.http import Http404
from django.shortcuts import get_object_or_404, render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question


class IndexView(generic.ListView):
    template_name = "application/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    template_name = "application/detail.html"
    model = Question


class ResultsView(generic.DetailView):
    template_name = "application/results.html"
    model = Question


class VoteView(generic.View):

    def post(self, request, question_id, *args, **kwargs):
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
