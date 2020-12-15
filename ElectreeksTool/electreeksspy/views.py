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



    smalltest = klasseFunktion() #halloTest()
    Mapping = {'smalltest': smalltest}
    return render(request, 'electreeksspy/index.html', Mapping)
