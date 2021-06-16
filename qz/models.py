from django.db import models


class Question(models.Model):
    question_uuid = models.BigAutoField(primary_key=True)
    question_text = models.CharField(max_length=200)

    choiceA = models.CharField(max_length=100, default='')
    choiceA_is_correct = models.BooleanField(default=False)

    choiceB = models.CharField(max_length=100, default='')
    choiceB_is_correct = models.BooleanField(default=False)

    choiceC = models.CharField(max_length=100, default='')
    choiceC_is_correct = models.BooleanField(default=False)

    choiceD = models.CharField(max_length=100, default='')
    choiceD_is_correct = models.BooleanField(default=False)


class Quiz(models.Model):
    # quiz can have 2-5 questions
    question1 = models.ForeignKey(Question, on_delete=models.CASCADE, default=None, related_name='question1')
    question2 = models.ForeignKey(Question, on_delete=models.CASCADE, default=None, related_name='question2')
    question3 = models.ForeignKey(Question, on_delete=models.CASCADE, default=None, related_name='question3', null=True, blank=True)
    question4 = models.ForeignKey(Question, on_delete=models.CASCADE, default=None, related_name='question4', null=True, blank=True)
    question5 = models.ForeignKey(Question, on_delete=models.CASCADE, default=None, related_name='question5', null=True, blank=True)
    quiz_uuid = models.BigAutoField(primary_key=True)
    quiz_title = models.CharField(max_length=100)
    # short description of the quiz
    about_quiz_text = models.CharField(max_length=250, default='')

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

