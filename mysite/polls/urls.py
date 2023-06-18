from django.urls import path
from . import views

app_name = 'polls'
# urlpatterns = [
#     path('',views.index, name='index'),
#     # eg: /polls/8/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # eg: /polls/8/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # eg: /polls/8/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # eg: /polls/8/
    path('<int:pk/', views.DetailView.as_view(), name='detail'),
    # eg: /polls/8/results/
    path('<int:pk/results/', views.ResultsView.as_view(), name='results'),
    # eg: /polls/8/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]