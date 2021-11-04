"""
Electreeks® SpyAgent
An App based on a Django framework

© Electreeks® - Hans Umlauft
"""

from django.shortcuts import render, redirect
from .objectrecognition import ObjectRecognition
from django.http import HttpResponse

from .models import *


print("\nW̳e̳l̳c̳o̳m̳e̳ ̳t̳o̳ ̳E̳l̳e̳c̳t̳r̳e̳e̳k̳s̳ ̳S̳p̳y̳A̳g̳e̳n̳t̳ v2.0!" )
print("\nThat's new in version 2.0:")
print("1. Add up to four streams to catch everything that's going on.")
print("2. Your streams will be stored locally and will remain beyond a reboot.")
print("3. Click on one of your streams to get to the image recognition screen.")
print("\nHelp: A streaming URL should look something like this:")
print("i.e      MotionEyeOS:   http://yourip:8081")
print("         MJPG-Streamer: http://yourip:8000/?action=stream")
print("\nNOTES: Electreeks SpyAgent is only optimized for Google Chrome")
print("- Electreeks SpyAgent works only fine with Google Chrome")
print("- To save Pi resources and avoid unwanted reboots,")
print("  we recommend to use MJPG-Streamer")
print("- Please remember that this will only work in your local network!")
print("  To enter your Camera from internet you have open a port for it.")
print("  Find more in the tutorials on https://electreeks.de \n")
# inputStream = input('Streaming URL: ')

# spyagent
# pass

# Site information
pagetitle = "Electreeks®"
subtitle = "Spyagent"
version = "2.0.0-local"
copyright = "© 2021 " + str(pagetitle) + " - Hans Umlauft"

def index(request):
    streams = Stream.objects.all()

    context = {
        'pagetitle': pagetitle,
        'subtitle': subtitle,
        'version': version,
        'copyright': copyright,
        'streams': streams
        }

    return render(request, 'electreeksspy/index.html', context)


def recognition(request, stream_id):
    stream = Stream.objects.get(pk=stream_id)

    recognizeObjects = ObjectRecognition()

    # Set a treshold between 0.0 and 1.0 for show a detected object
    confidenceTreshold = .50

    # Start object recognition
    recognizedObjects = recognizeObjects.doRecognition(stream.streaming_url, confidenceTreshold)

    context = {
        'pagetitle': pagetitle,
        'subtitle': subtitle,
        'version': version,
        'copyright': copyright,
        'recognizedObjects': recognizedObjects,
        'stream': stream,
        }

    return render(request, 'electreeksspy/recognition.html', context)

def fullscreen(request, stream_id):
    stream = Stream.objects.get(pk=stream_id)

    context = {
        'pagetitle': pagetitle,
        'subtitle': subtitle,
        'version': version,
        'copyright': copyright,
        'stream': stream
        }

    return render(request, 'electreeksspy/fullscreen.html', context)

def delete(request, stream_id):
    stream = Stream.objects.get(pk=stream_id)
    stream.delete()
    streams = Stream.objects.all()

    context = {
        'pagetitle': pagetitle,
        'subtitle': subtitle,
        'version': version,
        'copyright': copyright,
        'streams': streams
        }

    return redirect('/')

def create(request):
    streaming_url = request.POST.get('streaming_url', None)
    camera_label = request.POST.get('camera_label', None)

    new_data = Stream(name=camera_label, streaming_url=streaming_url)
    new_data.save()


    return redirect('/')
