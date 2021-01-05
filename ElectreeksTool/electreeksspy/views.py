from django.shortcuts import render
import numpy as np
import cv2
import matplotlib.pyplot as plt
from .objectrecognition import ObjectRecognition
# Create your views here.

def index(request):

    def klasseFunktion():
        #img = cv2.imread("dummybild.jpg", -1)
        recogniseObjects = ObjectRecognition()
        recogniseObjects.start()


        #return print(image.shape)
        #plt.imshow(a)
        #cv.waitKey(0)
        #cv.destroyAllWindows()
        #return img


    objecthandler = ObjectRecognition()
    recognized_object = objecthandler.recognizedobject
    Mapping = {'recognized_object': recognized_object}
    return render(request, 'electreeksspy/index.html', Mapping)
