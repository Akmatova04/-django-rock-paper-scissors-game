# gamecore/urls.py
from django.urls import path
from . import views # биздин views.py файлынан көрүнүштөрдү импорттоо

urlpatterns = [
    # Оюндун негизги барагы
    path('play/', views.play_rps_view, name='play_rps_url'),
    
    # Упайларды тазалоо үчүн URL
    path('reset/', views.reset_scores_view, name='reset_scores_url'),
]