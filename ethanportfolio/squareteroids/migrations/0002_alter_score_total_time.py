# Generated by Django 4.1 on 2022-08-21 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squareteroids', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='total_time',
            field=models.DurationField(null=True),
        ),
    ]
