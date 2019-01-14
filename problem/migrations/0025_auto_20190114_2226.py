# Generated by Django 2.1.4 on 2019-01-14 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0024_auto_20190114_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='statement',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='test',
        ),
        migrations.AddField(
            model_name='statement',
            name='problem',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='problem.Problem'),
        ),
        migrations.AddField(
            model_name='test',
            name='problem',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='problem.Problem'),
        ),
    ]
