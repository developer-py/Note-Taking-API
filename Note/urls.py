from django.urls import path
from .views import NoteListCreateAPIView, NoteRetrieveUpdateAPIView

urlpatterns = [
    path('notes/', NoteListCreateAPIView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteRetrieveUpdateAPIView.as_view(), name='note-retrieve-update'),
 ]