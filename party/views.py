from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Party
from .serializers import PartySerializer
from .utils import getRoutes
from rest_framework import generics

# Create your views here.
class PartyList(generics.ListCreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

class PartyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer    


@api_view(['GET'])
def getAllRoutes(request):
    return Response(getRoutes(request))


# @api_view(['POST'])
# def createParty(request):
#     print('DATA ===>', request.data)
#     if(request.method == 'POST'):
#         data = request.data
#         party = Party.objects.create(
#             name=data['name'],
#             description=data['description'],
#             date=data['date'],
#             time=data['time'],
#             location=data['location'],
#             image=data['image'],
#     )
#         serializer = PartySerializer(party, many=False)    
#         return Response(serializer.data)
#     else:
#         return Response('Error')


# @api_view(['GET'])
# def getParties(request):
#     if(request.method == 'GET'):
#         parties = Party.objects.all().order_by('-created_at')
#         serializer = PartySerializer(parties, many=True)
#         return Response(serializer.data)
#     else:
#         return Response('Error')


# @api_view(['GET'])
# def getParty(request, pk):
#     if(request.method == 'GET'):
#         party = Party.objects.get(id=pk)
#         serializer = PartySerializer(party, many=False)
#         return Response(serializer.data)
#     else:
#         return Response('Error')

          
# @api_view(['PUT'])
# def updateParty(request, pk):
#     if(request.method == 'PUT'):
#         data = request.data
#         party = Party.objects.get(id=pk)
#         serializer = PartySerializer(instance=party, data=data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response('Error')


# @api_view(['DELETE'])
# def deleteParty(request, pk):
#     if(request.method == 'DELETE'):
#         party = Party.objects.get(id=pk)
#         party.delete()
#         return Response('Party deleted')
#     else:
#         return Response('Error')        
    