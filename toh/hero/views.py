from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero

@csrf_exempt
def hero_list(request):
  if request.method == 'GET':
    hero_all_list = [hero for hero in Hero.objects.all().values()]
    return JsonResponse(hero_all_list, safe=False)
  elif request.method == 'POST':
    try:
      body = request.body.decode()
      hero_name = json.loads(body)['name']
      hero_age = json.loads(body)['age']
    except (KeyError, JSONDecodeError) as e:
      return HttpResponseBadRequest()
    hero = Hero(name=hero_name, age=hero_age)
    hero.save()
    response_dict = {'id': hero.id, 'name': hero.name, 'id': hero.age}
    return JsonResponse(response_dict, status=201)
  else:
    return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id=0):
  if request.method == 'GET':
    hero_all_list = [hero for hero in Hero.objects.filter(id=id).values()]
    return JsonResponse(hero_all_list, safe=False)
  if request.method == 'PUT':
    try:
      body = request.body.decode()
      hero_name = json.loads(body)['name']
      hero_age = json.loads(body)['age']
    except (KeyError, JSONDecodeError) as e:
      return HttpResponseBadRequest()
    hero = Hero.objects.filter(id=id)[0]
    hero.name = hero_name
    hero.age = hero_age
    hero.save()
    response_dict = {'id': id, 'name': hero.name, 'age': hero.age}
    return JsonResponse(response_dict, status=201)
  else:
    return HttpResponseNotAllowed(['GET', 'PUT'])
    