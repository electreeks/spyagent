import numpy as np
import cv2


class ObjectRecognition():
    """
    Class for Objectrecognition. Capture Frame and find objects based on model an treshold.
    doRecognition - Triggered by JS/Ajax #js_page_refresher.
    returns dictionary with object name and confidence.
    """

    def __init__ (self):
        # Pretrained classes in the model
        self.__ObjectsNames = {0: 'background',
                      1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus',
                      7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light', 11: 'fire hydrant',
                      13: 'stop sign', 14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat',
                      18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
                      24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 31: 'handbag',
                      32: 'tie', 33: 'suitcase', 34: 'frisbee', 35: 'skis', 36: 'snowboard',
                      37: 'sports ball', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
                      41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
                      46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon',
                      51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange',
                      56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut',
                      61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed',
                      67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop', 74: 'mouse',
                      75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 79: 'oven',
                      80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book', 85: 'clock',
                      86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier', 90: 'toothbrush'}



        # Get user stream
        self.__cap = cv2.VideoCapture(0)

        # Loading models
        self.__model = cv2.dnn.readNetFromTensorflow('models/frozen_inference_graph.pb',
                                              'models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

        # Dictionary which will cerry the objectname (key) and the confidence (value)
        self.recognized_objects = {}

    def doRecognition(self):
        # Capture frame
        ret, image = self.__cap.read()

        #Getting height and shape of image
        image_height, image_width, _ = image.shape

        blob=cv2.dnn.blobFromImage(image, size=(299, 299), swapRB=True)

        #set blob as input to model
        self.__model.setInput(cv2.dnn.blobFromImage(image, size=(299, 299), swapRB=True))


        def id_Object_class(class_id, classes):
            for key_id, class_name in classes.items():
                if class_id == key_id:
                    return class_name

        output = self.__model.forward()
            #print(output[0,0,:,:])
            #print(output)
        for detection in output[0, 0, :, :]:
            confidence = detection[2]       #confidence for occuring a class
                #print(detection[2])
            if confidence > .60:            #threshold
                class_id = detection[1]
                #print(detection[1])
                class_name=id_Object_class(class_id,self.__ObjectsNames)       #calling id_Object_class function
                #print(str(str(class_id) + " " + str(detection[2])  + " " + class_name))
                box_x = detection[3] * image_width
                box_y = detection[4] * image_height
                box_width = detection[5] * image_width
                box_height = detection[6] * image_height
                cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width),
                                    int(box_height)), (23, 230, 210), thickness=1) #drawing rectangle
                cv2.putText(image,class_name ,(int(box_x), int(box_y+.05*image_height)),
                cv2.FONT_HERSHEY_SIMPLEX,(.005*image_width),(0, 0, 255)) #text
                self.recognized_objects[class_name.capitalize()] = "{:.2f}".format(detection[2])

        return self.recognized_objects
        #self.__cap.release()
        #cv2.destroyAllWindows()
