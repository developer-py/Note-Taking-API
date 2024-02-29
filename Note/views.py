from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer
from django.shortcuts import get_object_or_404 


class NoteListCreateAPIView(APIView):
    def get(self, request):
        title_substr = request.query_params.get('title', '')
        if title_substr:
            notes = Note.objects.filter(title__icontains=title_substr)
        else:
            notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteRetrieveUpdateAPIView(APIView):
    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def put(self, request, pk):
        if not request.path.endswith('/'):
            return Response(status=status.HTTP_301_MOVED_PERMANENTLY, headers={'Location': request.path + '/'})
        note = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):  # Adding patch method
        note = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(note, data=request.data, partial=True)  # Using partial=True for partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
