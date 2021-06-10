from django.contrib import admin
from .models import Question, Quiz


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_uuid', 'question_text')


class QuizAdmin(admin.ModelAdmin):
    list_display = ('quiz_uuid', 'quiz_title')


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
# Register your models here.
