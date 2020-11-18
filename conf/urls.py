from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from surveys.views import MainView, MyLoginView, MyRegisterView, SurveyView, SurveyListView, SuccessView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('register', MyRegisterView.as_view(), name='register'),
    path('login', MyLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('survey', SurveyListView.as_view(), name='survey_list'),
    path('survey/<int:id>', SurveyView.as_view(), name='survey'),
    path('success', SuccessView.as_view(), name='success')
]
