import datetime
import os

from authlib.django.client import OAuth
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse

from dotenv import load_dotenv, find_dotenv

from oauth_poc.models import OAuth2Token

load_dotenv(find_dotenv())

RACO_CLIENT_ID = os.getenv('RACO_CLIENT_ID')
RACO_CLIENT_SECRET = os.getenv('RACO_CLIENT_SECRET')
RACO_AUTH_URL = os.getenv('RACO_AUTH_URL')

oauth = OAuth()
oauth.register('raco',
               client_id=RACO_CLIENT_ID,
               client_secret=RACO_CLIENT_SECRET,
               request_token_url=None,
               request_token_params=None,
               access_token_url='https://api.fib.upc.edu/v2/o/token',
               access_token_params=None,
               refresh_token_url=None,
               authorize_url='https://api.fib.upc.edu/v2/o/authorize',
               api_base_url='https://api.fib.upc.edu/v2/',
               client_kwargs={'response_type': 'code', 'scope': 'read', 'approval_prompt': 'force'},
               )


def index(request):
    return render_to_response('index.html')

def login(request):
    # build a full authorize callback uri
    redirect_uri = request.build_absolute_uri('/oauth/authorize')
    return oauth.raco.authorize_redirect(request, redirect_uri)

def authorize(request):
    print(request)
    token = oauth.raco.authorize_access_token(request)
    print(token)

    model = OAuth2Token(access_token=token['access_token'],
                        token_type=token['token_type'],
                        refresh_token=token['refresh_token'],
                        expires_at=int(token['expires_at']))
    print(model.access_token)
    model.save()
    return render_to_response('index.html')

def fetch_resource(request):
    print(request)
    token = OAuth2Token.objects.first()
    # remember to assign user's token to the client
    resp = oauth.raco.get('/v2/jo/avisos/?format=json', token=token.to_token())
    profile = resp.json()
    return JsonResponse(profile)