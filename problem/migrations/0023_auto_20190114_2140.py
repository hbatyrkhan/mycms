# Generated by Django 2.1.4 on 2019-01-14 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0022_auto_20190114_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statement',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='test',
            name='problem',
        ),
        migrations.AddField(
            model_name='problem',
            name='statement',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='problem.Statement'),
        ),
        migrations.AddField(
            model_name='problem',
            name='test',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='problem.Test'),
        ),
    ]
