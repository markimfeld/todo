# Generated by Django 3.0.6 on 2020-05-19 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20200519_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listtask',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='tasks.Tag'),
        ),
    ]
