# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
# 'Render'는 사이트를 보여준다. (경우 4)
from django.http import HttpResponse, Http404
# HttpResponse는 메시지만 띄운다. (경우 1~3)
from django.template import loader

from .models import Question, Choice

def index(request):
    # return HttpResponse(output)
    # output = ', '.join([q.question_text for q in latest_question_list])
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
# 경우 1 : 텍스트만 보여준다.
# 경우 2 : 저장된 값을 보여준다.
# 경우 3 : 템플릿을 사용한다. 현재 적용 중)
# 경우 4 : render()를 사용하여 경우 3을 보완한다.

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "질문 %s의 결과를 찾으시는군요."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 투표용 폼을 다시 보여준다.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "선택하지 않으셨습니다.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터를 제대로 받아오면 항상
        # HttpResponseRedirect를 반환한다.
        # 이는 사용자가 뒤로가기 버튼을 눌렀을 때
        # 데이터가 두 번 등록되는 상황을 막아준다.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))