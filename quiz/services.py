from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from typing import List
from django.shortcuts import render
from django.http import HttpResponse


class QuizResultService():
    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto

    def get_result(self) -> float:
        right_answers_by_user = 0
        right_answer = []
        questions_num = 0

        for question in self.quiz_dto.questions:
            for choice in question[2]:
                if choice.is_correct:
                    right_answer.append(choice.uuid)

            if right_answer == self.answers_dto.answers[questions_num][1]:
                right_answers_by_user += 1
            questions_num += 1
            right_answer = []
        print(questions_num, right_answers_by_user)
        if questions_num == right_answers_by_user:
            return 1
        return 1.00 - float((questions_num - right_answers_by_user) / questions_num)

        # your code here
