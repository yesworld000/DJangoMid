from api.models import Book, Journal
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

from api.serializers import BookSerializer, JournalSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register_page(request):
    # if request.user.is_authenticated():
    #     return redirect('home')
    # else:
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, 'Welcome to us, '+name+'!')

            return redirect('login')

    context = {"form": form}
    return render(request, 'accounts/registration.html', context)


def login_page(request):
    # if request.user.is_authenticated():
    #     return redirect('home')
    # else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # return redirect('register')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def books_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        books_json = [books.to_json() for book in books]
        return JsonResponse(books_json, safe=False)
    elif request.method == 'PUT':
        s = BookSerializer(instance=books, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response({'error': s.errors})
    elif request.method == 'DELETE':
        books.delete()
        return JsonResponse({'deleted': True})


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def journals_list(request):
    if request.method == 'GET':
        journals = Journal.objects.all()
        journals_json = [journals.to_json() for journals in Journal]
        return JsonResponse(journals_json, safe=False)
    elif request.method == 'PUT':
        s = JournalSerializer(instance=book, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response({'error': s.errors})
    elif request.method == 'DELETE':
        journals.delete()
        return JsonResponse({'deleted': True})

