# Generated by Django 4.0.3 on 2023-10-05 08:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0006_question_voter_alter_answer_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='voter',
            field=models.ManyToManyField(related_name='voter_answer', to=settings.AUTH_USER_MODEL),
        ),
    ]
