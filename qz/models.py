from django.db import models


class Question(models.Model):
    question_uuid = models.BigAutoField(primary_key=True)
    question_text = models.CharField(max_length=100)
    choiceA = models.CharField(max_length=100, default='')
    choiceA_is_correct = models.BooleanField(default=False)
    choiceB = models.CharField(max_length=100, default='')
    choiceB_is_correct = models.BooleanField(default=False)
    choiceC = models.CharField(max_length=100, default='')
    choiceC_is_correct = models.BooleanField(default=False)
    choiceD = models.CharField(max_length=100, default='')
    choiceD_is_correct = models.BooleanField(default=False)


class Quiz(models.Model):
    question1 = models.ForeignKey(Question, on_delete=models.CASCADE, default=None, related_name='question1')
    question2 = models.ForeignKey(Question, on_delete=models.CASCADE, default=None, related_name='question2')
    question3 = models.ForeignKey(Question, on_delete=models.CASCADE, default=None, related_name='question3')
    question4 = models.ForeignKey(Question, on_delete=models.CASCADE, default=None, related_name='question4')
    question5 = models.ForeignKey(Question, on_delete=models.CASCADE, default=None, related_name='question5')
    quiz_uuid = models.BigAutoField(primary_key=True)
    quiz_title = models.CharField(max_length=100)
    about_quiz_text = models.CharField(max_length=200, default='')

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

# class Answers(models.Model):
#    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#    question_id = models.ForeignKey(question, on_delete=models.CASCADE)
#    answers = models.
