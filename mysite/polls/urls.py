from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    # eg: /polls/8/
    path('<int:question_id>/', views.detail, name='detail'),
    # eg: /polls/8/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # eg: /polls/8/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]