# Generated by Django 3.0.6 on 2020-05-18 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200517_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='list_task',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tasks.ListTask'),
        ),
    ]