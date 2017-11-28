from django.shortcuts import get_object_or_404, render
# 'Render' makes the site. (Case 4)
from django.http import HttpResponse, Http404
# HttpResponse just shows the message. (Case 1~3)
from django.template import loader

from .models import Question, Choice

def index(request):
    # return HttpResponse(output)
    # output = ', '.join([q.question_text for q in latest_question_list])
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
# Case 1 : Just showing text
# Case 2 : Showing the saved value
# Case 3 : Using template (current)
# Case 4 : Fixing the Case 3, using render()

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "질문 %s의 결과를 찾으시는군요."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("질문 %s에 투표하셨습니다." % question_id)
# Create your views here.
