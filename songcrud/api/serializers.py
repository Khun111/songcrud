from django.db.models import fields
from rest_framework import serializers
from musicapp.models import Artiste, Song, Lyric

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = "__all__"
'''
class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ('song_id', 'content')
'''