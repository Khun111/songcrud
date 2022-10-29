from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    #path('artistes/', views.artiste_list),
    #path('artistes/<int:id>', views.artiste_detail),
    path('songs/', views.song_list),
    path('songs/<int:id>', views.song_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)