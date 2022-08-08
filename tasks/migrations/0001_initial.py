# Generated by Django 4.0.7 on 2022-08-08 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', models.TextField(blank=True, max_length=255, null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date and time when created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='date and time when last modified')),
                ('status', models.CharField(choices=[('todo', 'To do'), ('in_progress', 'In progress'), ('on_hold', 'On hold'), ('done', 'Done')], default='in_progress', max_length=128, verbose_name='status')),
                ('due_date', models.DateField(blank=True, null=True, verbose_name='due date')),
                ('priority', models.CharField(choices=[('low', 'Low priority'), ('medium', 'Medium priority'), ('high', 'High priority')], default='medium', max_length=128, verbose_name='priority')),
                ('task_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lists.list', verbose_name='list')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'task',
                'verbose_name_plural': 'tasks',
            },
        ),
    ]
