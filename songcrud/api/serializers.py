from django.db.models import fields
from rest_framework import serializers
from musicapp.models import Artiste, Song, Lyric

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ('id', 'first_name', 'last_name', 'age')

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('artiste_id', 'title', 'date_released', 'likes')
class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ('song_id', 'content')