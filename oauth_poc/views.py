import datetime
import os

from django.contrib.auth import authenticate, login
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, JsonResponse

from main.models import OAuth2Token
from main.oauth import oauth

def index(request):
    return render_to_response('index.html')

def login_raco(request):
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
    model.user = request.user
    model.save()
    return redirect('index')

def fetch_resource(request):
    print(request)
    token = request.user.oauth2token
    # remember to assign user's token to the client
    resp = oauth.raco.get('/v2/jo/avisos/?format=json', token=token.to_token())
    profile = resp.json()
    return JsonResponse(profile)

from django.contrib.auth.models import User

def register(request):
    login_word = request.POST['login']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(login_word, email, password)
    user.save()
    login(request, authenticate(request, username=login_word, password=password))
    return redirect('login')
