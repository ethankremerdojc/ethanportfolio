from django.contrib import admin
from squareteroids.models import Score, Difficulty

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('username', 'timestamp', 'difficulty', 'time')
    readonly_fields = ('timestamp', )
    fields = (
        ('username'), 
        ('start_time', 'end_time', 'total_time'), 
        'difficulty', 
        ('timestamp')
    )

admin.site.register(Score, ScoreAdmin)
admin.site.register(Difficulty)