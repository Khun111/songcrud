# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from musicapp.models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer, SongSerializer
from rest_framework import serializers
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Api Overview': '/',
        'Artiste List': '/artistes',
        'Artiste Detail': '/artistes/id',
        'Song List': '/songs',
        'Song Detail': '/songs/id',
    }
    return Response(api_urls)

@api_view(['GET', 'POST'])
def artiste_list(request, format=None):
    if request.method == 'GET':
        artistes = Artiste.objects.all()
        serializer = ArtisteSerializer(artistes, many=True)
        return Response({'artistes': serializer.data})
    if request.method == 'POST':
        serializer = ArtisteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def artiste_detail(request, id, format=None):
    try:
        artiste = Artiste.objects.get(pk=id)
    except Artiste.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtisteSerializer(artiste)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArtisteSerializer(artiste, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        artiste.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'POST'])
def song_list(request, format=None):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response({'Songs': serializer.data})
    if request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, id, format=None):
    try:
        song = Song.objects.get(pk=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        song.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)