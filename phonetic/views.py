from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from text2ipa import get_IPA
from traductorPy import Traductor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




def index(request):
    data = request.GET
    text = data.get('text')
    language = 'am'
    ipa = get_IPA(text,language)
    return JsonResponse({'message': ipa})