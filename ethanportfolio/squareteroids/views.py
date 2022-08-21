import json

from django.shortcuts import render
from django.http import Http404, HttpResponse
from datetime import datetime

from django.utils import timezone
from datetime import timedelta
from squareteroids.models import Score, Difficulty

def squareteroids(request, *args, **kwargs):
    template_name = "game/index.html"
    context = {}
    all_difficulties = Difficulty.objects.all().order_by('starting_enemy_speed')

    highest_scores = {}
    for d in all_difficulties:
        highest_score = Score.get_highest_score(difficulty=d)

        if not highest_score:
            highest_score = {
                'username': 'anonymous',
                'time': '00:00:00'
            }
        else:
            highest_score = {
                'username': highest_score.username,
                'time': highest_score.time
            }

        highest_scores[d.name] = highest_score

    context['highest_scores'] = highest_scores
    context['difficulties'] = sorted([ dif.to_dict() for dif in Difficulty.objects.all() ], key= lambda dif: dif['starting_enemy_speed'])

    return render(request, template_name, context)

def end_time(request, *args, **kwargs):
    data = json.loads(request.body)

    score = Score.objects.get(id=data['scoreId'])
    score.end_time = timezone.now() + timedelta(seconds=1)
    total_time = score.end_time - score.start_time
    score.total_time = total_time
    score.save()

    return HttpResponse(json.dumps({"time": str(score.time)}), content_type="application/json")

def start_time(request, *args, **kwargs):
    data = json.loads(request.body)
    difficulty = Difficulty.objects.get(name=data.get('difficulty'))

    new_score = Score.objects.create(
        username=data.get('username'),
        difficulty=difficulty,
        start_time=timezone.now()
    )

    return HttpResponse(json.dumps({"id": new_score.id}), content_type="application/json")