from django.shortcuts import render

# Create your views here.

def send_message(requets):
    return render(requets,'contact.html')