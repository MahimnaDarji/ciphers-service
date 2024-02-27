from django.shortcuts import render
from django.http import JsonResponse

from .ciphers import caesar_encoding

def greeting(request):
    res = {'message': 'Welcome to the Ciphers Service!'}
    return JsonResponse(res)

def encode(request, plaintext, shift):
    params = dict(request.GET)
    print(params)
    cipher = caesar_encoding(plaintext, int(shift))
    return JsonResponse({'cipher': cipher})
