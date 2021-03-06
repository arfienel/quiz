# Generated by Django 3.2 on 2021-06-16 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qz', '0008_quiz_about_quiz_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='about_quiz_text',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question3',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question3', to='qz.question'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question4',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question4', to='qz.question'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question5',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question5', to='qz.question'),
        ),
    ]
