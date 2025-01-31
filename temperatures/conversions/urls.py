from django.urls import path, include
from . import views 

urlpatterns = [
    path ('', views.convert, name="convert"),
    path ('results/', views.results, name="results"),
    path ('create/', views.create, name="create"),
    path("historique/<str:username>", views.historique, name="historique")
    
]
