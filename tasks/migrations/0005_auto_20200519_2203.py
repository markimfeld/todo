# Generated by Django 3.0.6 on 2020-05-19 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20200519_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='list_task',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.ListTask'),
        ),
    ]
