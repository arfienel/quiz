# Generated by Django 3.1.7 on 2021-06-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qz', '0007_auto_20210603_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='about_quiz_text',
            field=models.CharField(default='', max_length=200),
        ),
    ]