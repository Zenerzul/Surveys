from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from surveys.forms import MyUserCreationForm
from surveys.models import Survey, Question


class MyRegisterView(CreateView):
    form_class = MyUserCreationForm
    success_url = 'login'
    template_name = 'surveys/register.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'surveys/login.html'


class MainView(View):
    def get(self, request):
        return render(request, 'surveys/main.html')


class SurveyView(View):
    def get(self, request, id):
        survey = Survey.objects.get(id=id)
        questions = Question.objects.filter(survey_id=id)
        for question in questions:
            if question.variants is not None:
                question.variants = list(question.variants.split())
        return render(request, 'surveys/single_survey.html', context={
            'survey': survey,
            'questions': questions,
        })

class SurveyListView(View):
    def get(self, request):
        surveys = Survey.objects.all()
        return render(request, 'surveys/survey_list.html', context={
            'surveys': surveys
        })
