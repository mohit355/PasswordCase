# Generated by Django 2.0.2 on 2019-01-07 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.RemoveField(
            model_name='case',
            name='answer1',
        ),
        migrations.RemoveField(
            model_name='case',
            name='answer2',
        ),
        migrations.RemoveField(
            model_name='case',
            name='answer3',
        ),
        migrations.RemoveField(
            model_name='case',
            name='answer4',
        ),
        migrations.RemoveField(
            model_name='case',
            name='answer5',
        ),
    ]
