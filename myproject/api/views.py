from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from base.models import *
from rest_framework.decorators import api_view
from .serializers import *

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializers(items, many=True)
    return Response(serializer.data)

@api_view(['DELETE', 'GET'])
def getItem(request, pk):
    item = get_object_or_404(Item,id=pk)
    if request.method == "GET":
        serializer = ItemSerializers(item)
        return Response(serializer.data)
    elif request.method == "DELETE":
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view()
def getStudent(request, pk):
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializers(student)
    return Response(serializer.data)


@api_view(['POST'])
def addStudent(request):
    serializer = StudentAddSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)