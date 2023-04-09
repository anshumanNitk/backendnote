from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializer import NoteSerializer


@api_view(['GET'])
def GetRoutes(request):
        
    routes = [
        {
            'Endpoint': '/Notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/Notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/Notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/Notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def GetNotes(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def GetNote(request,pk):
    note=Note.objects.get(id=pk)
    serializer = NoteSerializer(note,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateNote(request):
    data=request.data
    note=Note.objects.create(
        body=data['body'])
    serializer= NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def UpadateNote(request,pk):
    data=request.data
    note=Note.objects.get(id=pk)
    serializer= NoteSerializer(instance=note,data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteNote(request,pk):
    note=Note.objects.get(id=pk)
    note.delete()
    return Response('note was deleted')
