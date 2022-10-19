from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    #url: .../polls/
    path('<int:question_id>/', views.detail, name='detail'),
    #url: .../polls/8/
    path('<int:question_id>/results/', views.results, name='results'),
    #url: .../polls/8/results/
    path('<int:question_id>/vote', views.vote, name='vote'),
    #url: .../polls/8/vote/
]