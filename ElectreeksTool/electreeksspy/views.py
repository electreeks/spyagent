from django.shortcuts import render
import numpy as np
import cv2
import matplotlib.pyplot as plt
from .objectrecognition import ObjectRecognition
# Create your views here.

def index(request):

    objecthandler = ObjectRecognition()
    recognized_object = objecthandler.doRecognition()
    Mapping = {'recognized_object': recognized_object}
    return render(request, 'electreeksspy/index.html', Mapping)
