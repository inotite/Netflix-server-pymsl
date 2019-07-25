from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse

import pymsl
import json

# Create your views here.

@api_view(['POST'])
def load_manifest(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        netflixid = data['netflixid']
        securenetflixid = data['securenetflixid']
        viewableid = int(data['viewableid'])

        user_auth_data = {
            'scheme': 'NETFLIXID',
            'authdata': {
                'netflixid': netflixid,
                'securenetflixid': securenetflixid
            }
        }

        client = pymsl.MslClient(user_auth_data)
        data = client.load_manifest(viewableid)
        print( client.load_manifest(viewableid) )

    return JsonResponse(data, safe = False)

@api_view(['POST'])
def load_manifest_email(request):
    if request.method == 'POST':
        netflixid = request.GET['email']
        securenetflixid = request.GET['password']
        viewableid = int(request.GET['viewableid'])

        user_auth_data = {
            'scheme': 'EMAIL_PASSWORD',
            'authdata': {
                'email': netflixid,
                'password': securenetflixid
            }
        }

        client = pymsl.MslClient(user_auth_data)
        data = client.load_manifest(viewableid)
        print( client.load_manifest(viewableid) )

    return JsonResponse(data, safe = False)    

