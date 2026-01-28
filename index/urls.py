from django.urls import path

from .views import home, stats, state_result, predict_pre, predict, predict_result


urlpatterns = [
    path('', home, name='index'),
    path('home/', home, name='index'),
    path('stats/', stats, name='states'),
    path('stats/result/', state_result, name='states-result'),
    path('predict/pre/', predict_pre, name='predict-pre'),
    path('predict/pre/player/', predict, name='predict'),
    path('predict/pre/player/result/', predict_result, name='predict-result'),
]

