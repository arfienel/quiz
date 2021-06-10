from django.urls import path
from .views import *


app_name = 'qz'
urlpatterns = [
    path('', main_page, name='main_page'),
    path('quiz/<int:quiz_uuid>/', quiz_start, name='quiz_start'),
    path('quiz/<int:quiz_uuid>/<int:question_uuid>/', quiz_process, name='quiz_process'),
    path('quiz/<int:quiz_uuid>/result', quiz_result, name='quiz_result')
]
