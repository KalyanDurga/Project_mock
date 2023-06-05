# Generated by Django 4.2.1 on 2023-06-03 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_alter_answer_username_alter_question_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qqq', to=settings.AUTH_USER_MODEL),
        ),
    ]
