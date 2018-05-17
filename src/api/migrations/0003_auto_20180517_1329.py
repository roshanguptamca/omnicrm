# Generated by Django 2.0.5 on 2018-05-17 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_session_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_type', models.CharField(choices=[('NOTE', 'Note'), ('TASK', 'Task')], max_length=20)),
                ('reference_id', models.CharField(max_length=50, null=True)),
                ('description', models.TextField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Session')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(choices=[('CASE', 'Case')], max_length=20)),
                ('krn', models.CharField(max_length=16, null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Task')),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Task'),
        ),
    ]
