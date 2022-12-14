# Generated by Django 4.1 on 2022-08-29 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('description', models.TextField()),
                ('page_link', models.CharField(max_length=255, null=True)),
                ('visible', models.BooleanField(default=False)),
            ],
        ),
    ]
