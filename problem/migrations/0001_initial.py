# Generated by Django 2.1.4 on 2019-03-07 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_id', models.IntegerField(default=0)),
                ('key', models.CharField(max_length=100)),
                ('secret', models.CharField(max_length=100)),
                ('testset_name', models.CharField(default='tests', max_length=100)),
                ('checker', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.TextField()),
                ('output', models.TextField(blank=True)),
                ('test_id', models.IntegerField()),
                ('in_statement', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('legend', models.TextField()),
                ('input', models.TextField()),
                ('output', models.TextField()),
                ('notes', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('time_limit', models.IntegerField()),
                ('memory_limit', models.IntegerField()),
                ('input_file', models.CharField(max_length=100)),
                ('output_file', models.CharField(max_length=100)),
                ('problem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='problem.Problem')),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Problem'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='test',
            order_with_respect_to='test_id',
        ),
        migrations.AddField(
            model_name='problem',
            name='contest',
            field=models.ManyToManyField(blank=True, to='contest.Contest'),
        ),
    ]
