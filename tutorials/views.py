from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse

from tutorials.models import Profil
from tutorials.serializers import ProfilSerializer
from tutorials.serializers import ClusterSerializer
from rest_framework.decorators import api_view
import pandas as pd
import csv

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    #Retrieve all Tutorials/ find by title
    """
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    """

    #Create and Save a new Tutorial:
    if request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = ProfilSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Delete all Tutorials from the database
    elif request.method == 'DELETE':
        count = Profil.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try:
        tutorial = Profil.objects.get(pk=pk)
    except Tutorial.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    #Find a single Tutorial with an id
    if request.method == 'GET':
        tutorial_serializer = ProfilSerializer(tutorial)
        return JsonResponse(tutorial_serializer.data)

    #Update a Tutorial by the id in the request:
    elif request.method == 'PUT':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = ProfilSerializer(tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a Tutorial with the specified id
    elif request.method == 'DELETE':
        tutorial.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def login(request):
    if request.method == "POST":
        c=0
        tutorial_data = JSONParser().parse(request)
        users = Profil.objects.all()
        for user in users.values():
            if(user['email'] == tutorial_data['email'] and user['password'] == tutorial_data['password']):
                return JsonResponse(user)
        return JsonResponse({'Login': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def clickstream(request) :
    if request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        print(tutorial_data)
        tutorial_serializer = ClusterSerializer(data=tutorial_data)
        print(tutorial_serializer)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def recommand(request) :
    if request.method == 'GET':
        return JsonResponse({'Login': 'Tutorial was deleted successfully!'},status=status.HTTP_201_CREATED)
