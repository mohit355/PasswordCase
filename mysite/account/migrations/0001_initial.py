# Generated by Django 2.1.1 on 2018-09-19 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('mobilenum', models.BigIntegerField()),
                ('ans1', models.CharField(max_length=100)),
                ('ans2', models.CharField(max_length=100)),
                ('ans3', models.CharField(max_length=100)),
                ('ans4', models.CharField(max_length=100)),
                ('ans5', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Passwords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=20)),
                ('uname', models.CharField(max_length=100)),
                ('eccrypted_password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='passwords',
            name='belongs_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Profile'),
        ),
        migrations.AddField(
            model_name='case',
            name='place',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.Profile'),
        ),
    ]
