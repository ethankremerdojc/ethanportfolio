# Generated by Django 4.1 on 2022-08-21 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squareteroids', '0002_alter_score_total_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='hours',
        ),
        migrations.RemoveField(
            model_name='score',
            name='minutes',
        ),
        migrations.RemoveField(
            model_name='score',
            name='seconds',
        ),
    ]