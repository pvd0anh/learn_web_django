from django.http import HttpResponse
from .models import Question

def index(request):
    return HttpResponse("Hello, world. My name is Doanh")


def detail(request, question_id):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def results(request, question_id):
    response = "You're looking for at results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
