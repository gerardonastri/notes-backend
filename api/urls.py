from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',  views.getRoutes, name="routes"),
    path('notes/',  views.getNotes, name="notes"),
    path('notes/create/', csrf_exempt(views.createNote), name="create-note"),
    path('notes/<str:pk>/update/', csrf_exempt(views.updateNote), name="update-note"),
    path('notes/<str:pk>/delete/', views.deleteNote, name="delete-note"),
    path('notes/<str:pk>',  views.getNote, name="note"),
]
