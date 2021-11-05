# spyagent
A simple remote raspberry pi camera stream view with object recognition from local pc

![alt text](https://electreeks.de/wp-content/uploads/2021/02/ai-raspberry-pi-objekterkennung-bilderkennung-electreeks-spy-agent.png)

# Welcome to Electreeks SpyAgent!

A simple tool for object recognition using http livestreams (i.e. of your Pi) with about 90 different object-classes. 

1. Start your App - 2. Enter a http streaming url - 3. Start object tracking by calling localhost:8000


## Installation

Open the terminal on your pc/Mac and do following steps:

**1. Clone the repo**

`git clone https://github.com/electreeks/spyagent.git`

***


**2. Change into the project folder**

`cd path-to-your-project/spyagent/ElectreeksTool`

***


**3. Install dependencies using pip**

Make sure that **pip** and **python** is installed and up-to-date.

`pip install django==3.1.2 numpy opencv-python`

Tested with following releases yet:
* python 3.8 / 3.9
* Django 3.1.x
* OpenCV-Python 4.4.x

***


**4. Create a live streaming / get http live-streaming-url - i.e. with a Raspberry Pi and a RPi Camera**


To create a live stream on your raspberry pi you can use MotionEyeOS, MJPG-Streamer, Motion ... to serve a http video stream.

**MotionEyeOS**

Check out our website to find the instructions for MotionEyeOS:
For English men. You may use the translation service of your browser 😉.

[Tutorial MotionEyeOS on Electreeks.de](https://electreeks.de/project/ueberwachungskamera-mit-motioneyeos/)

The default streaming-url of MotionEyeOS:
http://ip-of-your-pi:8081


**MJPG-Streamer**

Check out the MJPG-Streamer GitHub Repo to find the instructions to set up a https stream.

[https://github.com/jacksonliam/mjpg-streamer](https://github.com/jacksonliam/mjpg-streamer)

default streaming url:
http://ip-of-your-pi:8000/?action=stream

***


**5. Start the Electreeks SpyAgent-Server in the project folder.**

`python3 manage.py runserver`

Enter the streaming url created above and press return.
Your server should now running!

***


**6. Open 127.0.0.1:8000 / localhost:8000 in your browser**

If everything went well you'll see your stream with the object tracking.

Have fun!


***


Object recognition need a lot of resources, therefore it's not sustainable to use it on a Raspberry Pi. That's why you should provide a stream via Raspberry Pi and run our tool on a pc using this streaming url!

SpyAgent is only optimized for Google Chrome - In other browser it may not automatically update the recognized objects

Disclaimer:
Do not use it on a server whose freely accessible from internet, because secret credentials aren't secured due GitHub publication. 

