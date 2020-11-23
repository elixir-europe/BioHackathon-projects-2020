from django.urls import path
from . import views

urlpatterns = [
    path('', views.MatchingRunListView.as_view(), name='index'),
    path('<int:pk>/', views.MatchingRunDetailView.as_view(), name='detail'),
    path('create', views.create, name='create'),
    path('about', views.about, name='about'),
]