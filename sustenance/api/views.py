from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
from api.models import Category, Benefit, Nutrient, Origin, Item
from api.serializers import CategorySerializer, BenefitSerializer, NutrientSerializer, ItemSerializer, OriginSerializer
from django.views.decorators.csrf import csrf_exempt


def categories(request):
    try:
        items = Category.objects.all().values('id', 'name').order_by('name')
        items_json = json.dumps(list(items), cls=DjangoJSONEncoder)
        return JsonResponse(items_json, safe=False)
    except Category.DoesNotExist:
        data = {}
        return JsonResponse(data, safe=False)


def category(request, category_id):
    try:
        items = Category.objects.filter(id=category_id).values('id', 'name')
        items_json = json.dumps(list(items), cls=DjangoJSONEncoder)
        print(items_json)
        return JsonResponse(items_json, safe=False)
    except Category.DoesNotExist:
        data = {}
        return JsonResponse(data, safe=False)


def benefits(request):
    try:
        items = Benefit.objects.all().values('id', 'name').order_by('name')
        items_json = json.dumps(list(items), cls=DjangoJSONEncoder)
        return JsonResponse(items_json, safe=False)
    except Benefit.DoesNotExist:
        data = {}
        return JsonResponse(data, safe=False)


def benefit(request, benefit_id):
    try:
        items = Benefit.objects.filter(id=benefit_id).values('id', 'name')
        items_json = json.dumps(list(items), cls=DjangoJSONEncoder)
        return JsonResponse(items_json, safe=False)
    except Benefit.DoesNotExist:
        data = {}
        return JsonResponse(data, safe=False)


def nutrients(request):
    try:
        items = Nutrient.objects.all().values('id', 'name').order_by('name')
        items_json = json.dumps(list(items), cls=DjangoJSONEncoder)
        return JsonResponse(items_json, safe=False)
    except Nutrient.DoesNotExist:
        data = {}
        return JsonResponse(data, safe=False)


def nutrient(request, nutrient_id):
    try:
        items = Nutrient.objects.filter(id=nutrient_id).values('id', 'name')
        items_json = json.dumps(list(items), cls=DjangoJSONEncoder)
        return JsonResponse(items_json, safe=False)
    except Nutrient.DoesNotExist:
        data = {}
        return JsonResponse(data, safe=False)


def origins(request):
    try:
        items = Origin.objects.all().values('id', 'name').order_by('name')
        items_json = json.dumps(list(items), cls=DjangoJSONEncoder)
        return JsonResponse(items_json, safe=False)
    except Origin.DoesNotExist:
        data = {}
        return JsonResponse(data, safe=False)


def origin(request, origin_id):
    try:
        items = Nutrient.objects.filter(id=origin_id).values('id', 'name')
        items_json = json.dumps(list(items), cls=DjangoJSONEncoder)
        return JsonResponse(items_json, safe=False)
    except Origin.DoesNotExist:
        data = {}
        return JsonResponse(data, safe=False)


def item_category(request, category_id):
    try:
        items = Item.objects.filter(item_categories=category_id).values('id', 'name', 'image').order_by('name')
        items_json = json.dumps(list(items), cls=DjangoJSONEncoder)
        return JsonResponse(items_json, safe=False)
    except Item.DoesNotExist:
        data = {}
        return JsonResponse(data, safe=False)


def item_nutrient(request, nutrient_id):
    try:
        items = Item.objects.filter(item_nutrients=nutrient_id).values('id', 'name').order_by('name')
        items_json = json.dumps(list(items), cls=DjangoJSONEncoder)
        return JsonResponse(items_json, safe=False)
    except Item.DoesNotExist:
        data = {}
        return JsonResponse(data, safe=False)


def item_benefit(request, benefit_id):
    try:
        items = Item.objects.filter(item_benefits=benefit_id).values('id', 'name').order_by('name')
        items_json = json.dumps(list(items), cls=DjangoJSONEncoder)
        return JsonResponse(items_json, safe=False)
    except Item.DoesNotExist:
        data = {}
        return JsonResponse(data, safe=False)
#
# def seasons(request):
#     return HttpResponse("You're at the seasons page")
#
#
# def season(request, season_id):
#     return HttpResponse("You're looking at season %s" % season_id)
#
#
# def recipes(request):
#     return HttpResponse("You're at the recipes page")
#
#
# def recipe(request, recipe_id):
#     return HttpResponse("You're looking at recipe %s" % recipe_id)
#
#
# def remedies(request):
#     return HttpResponse("You're at the remedy page")
#
#
# def remedy(request, remedy_id):
#     return HttpResponse("You're looking at remedy %s" % remedy_id)
#
#
#
