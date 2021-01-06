from django.shortcuts import render
from .objectrecognition import ObjectRecognition

def index(request):

    # New Instance for class ObjectRecognition
    objecthandler = ObjectRecognition()

    # Start object recognition
    recognized_objects = objecthandler.doRecognition()

    # Site information
    pagetitle = "Electreeks®"
    subtitle = "Spyagent"

    context = {'pagetitle': pagetitle, 'subtitle': subtitle, 'recognized_objects': recognized_objects}

    return render(request, 'electreeksspy/index.html', context)
