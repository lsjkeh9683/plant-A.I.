from django.shortcuts import render, redirect
import RPi.GPIO as GPIO

pan = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(pan, GPIO.OUT)

def index(request):
    if 'on' in request.POST:
        GPIO.output(pan, GPIO.HIGH)
        return render(request, 'index.html')
    
    elif 'off' in request.POST:
        GPIO.output(pan, GPIO.LOW)
        return render(request, 'index.html')
    
    else:
        return render(request, 'index.html')