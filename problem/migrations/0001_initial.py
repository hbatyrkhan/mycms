# Generated by Django 2.1.4 on 2019-01-09 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idOfProblem', models.IntegerField(default=0)),
                ('key', models.CharField(max_length=100)),
                ('secret', models.CharField(max_length=100)),
            ],
        ),
    ]
