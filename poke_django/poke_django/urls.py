"""poke_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from trainer.views import TrainerCreate, TrainerGetUpdateDestroy
from teams.views import TeamCreate, TeamGetUpdateDestroy
from teams.views import AddPokemonToTeam, DeletePokemonFromTeam, GetallTeams

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trainer/create/', TrainerCreate.as_view()),
    path('trainer/delete/<int:pk>/', TrainerGetUpdateDestroy.as_view()),
    path('trainer/get/<int:pk>/', TrainerGetUpdateDestroy.as_view()),
    path('trainer/update/<int:pk>/', TrainerGetUpdateDestroy.as_view()),
    path('teams/create/', TeamCreate.as_view()),
    path('teams/delete/<int:pk>/', TeamGetUpdateDestroy.as_view()),
    path('teams/get/<int:pk>/', TeamGetUpdateDestroy.as_view()),
    path('teams/add/', AddPokemonToTeam.as_view()),
    path('teams/delete/<int:_pk>/<int:slot>/', DeletePokemonFromTeam.as_view()),
    path('teams/getall/<int:_id>/', GetallTeams.as_view()),
]
