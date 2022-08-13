# Generated by Django 4.1 on 2022-08-13 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_enemy_speed', models.FloatField()),
                ('starting_enemy_spawn_factor', models.FloatField()),
                ('enemy_speed_incremental_factor', models.FloatField()),
                ('enemy_spawn_incremental_factor', models.FloatField()),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seconds', models.IntegerField(null=True)),
                ('minutes', models.IntegerField(null=True)),
                ('hours', models.IntegerField(null=True)),
                ('enemy_speed', models.FloatField(null=True)),
                ('enemy_spawn_factor', models.FloatField(null=True)),
                ('username', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('difficulty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='squareteroids.difficulty')),
            ],
        ),
    ]