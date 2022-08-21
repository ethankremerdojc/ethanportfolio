from django.db import models

class Difficulty(models.Model):
    starting_enemy_speed = models.FloatField()
    starting_enemy_spawn_factor = models.FloatField()

    enemy_speed_incremental_factor = models.FloatField()
    enemy_spawn_incremental_factor = models.FloatField()

    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.name}"

    def to_dict(self) -> str:
        return {
            'name': self.name,
            'starting_enemy_speed': self.starting_enemy_speed,
            'starting_enemy_spawn_factor': self.starting_enemy_spawn_factor,
            'enemy_speed_incremental_factor': self.enemy_speed_incremental_factor,
            'enemy_spawn_incremental_factor': self.enemy_spawn_incremental_factor,
        }

class Score(models.Model):
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    total_time = models.DurationField(null=True)

    enemy_speed = models.FloatField(null=True)
    enemy_spawn_factor = models.FloatField(null=True)

    username = models.CharField(max_length=255)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.username} - {self.total_time}"

    @property
    def timestamp(self):
        return self.start_time

    @property
    def time(self):
        hours, remainder = divmod(self.total_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        def get_0_padded(num):
            if len(str(num)) == 1:
                return f"0{num}"
            return str(num)

        return f"{get_0_padded(hours)}:{get_0_padded(minutes)}:{get_0_padded(seconds)}"

    def get_highest_score(difficulty):
        return Score.objects.filter(
            difficulty=difficulty).order_by('total_time').last()