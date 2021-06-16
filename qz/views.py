from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.http import HttpResponse
from django.urls import reverse
from .models import Question, Quiz
from django.core.paginator import Paginator
import sys
from quiz.services import QuizResultService
from quiz import dto
from quiz.dto import *
from typing import List


# главная страница
def main_page(request):
    quiz_list = Quiz.objects.order_by('quiz_uuid')

    return render(request, 'main_page.html', {'quiz_list': quiz_list})


# start of the quiz
def quiz_start(request, quiz_uuid):
    try:
        quiz = get_object_or_404(Quiz, quiz_uuid=quiz_uuid)
    except:
        raise Http404('there are not such quiz ;(')

    # getting text and id of every question
    questions_list = [quiz.question1, quiz.question2, quiz.question3, quiz.question4, quiz.question5]
    questions_list_text, questions_id_list = [], []
    for item in questions_list:
        if not item:
            continue
        questions_list_text.append(item.question_text)
        questions_id_list.append(item.question_uuid)

    request.session['questions_id_list'] = questions_id_list

    return render(request, 'quiz_start.html', {'quiz': quiz, 'questions_list': questions_list_text, 'page': 0})


# passing the quiz
def quiz_process(request, quiz_uuid, question_uuid):

    # redirecting if last question
    if question_uuid == len(request.session['questions_id_list']):
        return redirect(reverse('qz:quiz_result', args=[quiz_uuid]))

    question = get_object_or_404(Question, question_uuid=request.session['questions_id_list'][question_uuid])
    try:
        request.session['answers']
    except:
        request.session['answers'] = {1: None, 2: None, 3: None, 4: None, 5: None}

    quiz_uuid = str(request.path_info)
    finder = quiz_uuid.find('quiz')
    quiz_uuid = quiz_uuid[finder + 5:quiz_uuid[finder + 5].find('/') - 2]

    # user pressed "next question" button
    if request.method == "POST":
        # all choices from question, user's choice will have the letter of the choice, otherwise it will be None
        answers_now = [request.POST.get('choiceA'), request.POST.get('choiceB'),
                       request.POST.get('choiceC'), request.POST.get('choiceD')]
        # getting user's answer on question
        for item in range(answers_now.count(None)):
            answers_now.remove(None)
        # saving user's answer on question
        request.session.modified = True
        request.session['answers'][str(question_uuid + 1)] = answers_now
        print(request.session['answers'])
        question_uuid += 1

        return redirect('qz:quiz_process', quiz_uuid, question_uuid)

    # checking question number, if it's last question, template will redirect to quiz_result
    if question_uuid <= len(request.session['questions_id_list'])-2:
        question_uuid += 1

    return render(request, 'quiz_process.html',
                  {'next_page': request.session['questions_id_list'][question_uuid], 'question': question,
                   'answers': request.session['answers'],
                   'quiz_uuid': quiz_uuid})


# finish of the quiz
def quiz_result(request, quiz_uuid):
    try:
        quiz = get_object_or_404(Quiz, quiz_uuid=quiz_uuid)
    except:
        raise Http404('no such quiz :(')
    answer_index = 1
    answers = []

    results_right_answers = []
    request.session.modified = True
    # filling dto classes, to check answers from services.QuizResultService
    # filling answers_dto
    for question in request.session['questions_id_list']:
        answer: List[dto.AnswerDTO] = [
            dto.AnswerDTO(
                question,
                request.session['answers'][str(answer_index)]

            )
        ]

        answer_index += 1
        answers.append(answer[0])

    answers_dto = dto.AnswersDTO(
        quiz_uuid,
        answers
    )
    questions = []
    # filling quiz_dto
    for question in request.session['questions_id_list']:
        question = get_object_or_404(Question, question_uuid=question)
        choices: List[dto.ChoiceDTO] = [
            dto.ChoiceDTO(
                "A",
                question.choiceA,
                question.choiceA_is_correct

            ),
            dto.ChoiceDTO(
                "B",
                question.choiceB,
                question.choiceB_is_correct

            ),
            dto.ChoiceDTO(
                "C",
                question.choiceC,
                question.choiceC_is_correct

            ),
            dto.ChoiceDTO(
                "D",
                question.choiceD,
                question.choiceD_is_correct

            ),
        ]
        right_answer = []
        for choice in choices:
            if choice[2] is True:
                right_answer.append(choice[0])
        results_right_answers.append(right_answer)
        question1: List[dto.QuestionDTO] = [
            dto.QuestionDTO(
                question.question_uuid,
                question.question_text,
                choices
            )
        ]

        questions.append(question1[0])

    quiz_dto = dto.QuizDTO(
        quiz.quiz_uuid,
        quiz.quiz_title,
        questions

    )

    # sending quiz_dto and answers_dto to check answers
    result = QuizResultService(quiz_dto, answers_dto)
    result = result.get_result()
    # user pressed "exit" button, clean session
    if request.method == "POST":
        del request.session['questions_id_list']
        del request.session['answers']
        return redirect(reverse('qz:main_page'))
    return render(request, 'quiz_result.html', {'result': round(result, 2),
                                                'result_answers': zip(
                                                    results_right_answers, list(request.session['answers'].values())),
                                                })

# Create your views here.
