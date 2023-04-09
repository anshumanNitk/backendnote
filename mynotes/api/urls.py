from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.GetRoutes,name='routes'),
    path('Notes/', views.GetNotes,name='Notes'),
    path('Notes/create/', views.CreateNote,name='create-note'),
    path('Notes/<str:pk>/update/', views.UpadateNote,name='updated-note'),
    path('Notes/<str:pk>/delete/', views.DeleteNote,name='deleted-note'),
    path('Notes/<str:pk>/', views.GetNote,name='Note'),
]
