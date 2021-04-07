import time
import webbrowser
import urllib.request
from os.path import expanduser
import os
import base64
import subprocess


def log(s):
    print("[AutoUBS] "+s)
    
pips = subprocess.check_output("pip3 list", shell=True, stderr=subprocess.STDOUT)

libs = ["PyAutoGUI", "opencv-python", "playsound"]

for lib in libs:
    if lib in str(pips):
        log(lib+" exists, skipping")
    else:
        os.system("pip install "+lib)

import pyautogui
import cv2
from playsound import playsound

webbrowser.open("https://workspace-zur3.ra.ubs.com/logon/choose-your-location/index.html", new=1, autoraise=True)

homeDIR = expanduser("~").replace("\\", "/")

time.sleep(3)

ressources = "../ressources/"

cLoc  = pyautogui.locateOnScreen(ressources+"country.png", confidence=0.7)
offset = (cLoc.width/7)
x, y = pyautogui.center(cLoc)
pyautogui.click(x+offset, y)

time.sleep(3)

mLoc  = pyautogui.locateCenterOnScreen(ressources+"mobile.png", confidence=0.9)
pyautogui.click(mLoc)
pyautogui.move(200,0)

dLoc = None

while(dLoc == None):
    playsound(ressources+"jingle.mp3")# sms
    time.sleep(15)
    dLoc  = pyautogui.locateCenterOnScreen(ressources+"download.png", confidence=0.9)

pyautogui.click(dLoc)


for file in os.listdir(homeDIR+"/Downloads"):
    if file.endswith(".ica"):
        os.system(file)
