"""
Electreeks® SpyAgent
An App based on a Django framework

© Electreeks® - Hans Umlauft
"""

from django.shortcuts import render
from .objectrecognition import ObjectRecognition


print("\nW̳e̳l̳c̳o̳m̳e̳ ̳t̳o̳ ̳E̳l̳e̳c̳t̳r̳e̳e̳k̳s̳ ̳S̳p̳y̳A̳g̳e̳n̳t̳!" )
print("\nTo start the Application, enter a valid Streaming URL of your Electreeks RPi Camera.")
print("i.e      MotionEyeOS:   http://yourip:8081")
print("         MJPG-Streamer: http://yourip:8000/?action=stream")
print("Please remember that this will only work in your local network!")
print("To enter your Camera from internet you have open a port for it.")
print("Find more in the tutorials on https://electreeks.de \n")
inputStream = input('Streaming URL: ')


def index(request):

    recognizeObjects = ObjectRecognition()

    # Site information
    stream = inputStream
    pagetitle = "Electreeks®"
    subtitle = "Spyagent"
    version = "1.0.0-beta.local"
    copyright = "© 2020 " + str(pagetitle) + " - Hans Umlauft"

    # Set a treshold between 0.0 and 1.0 for show a detected object
    confidenceTreshold = .50

    # Start object recognition
    recognizedObjects = recognizeObjects.doRecognition(inputStream, confidenceTreshold)

    context = {
        'pagetitle': pagetitle,
        'subtitle': subtitle,
        'version': version,
        'copyright': copyright,
        'recognizedObjects': recognizedObjects,
        'stream': stream
        }

    return render(request, 'electreeksspy/index.html', context)
