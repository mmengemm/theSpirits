import time
import webbrowser
import urllib.request
from os.path import expanduser
import os
import base64
import subprocess


def log(s):
    print("[AutoUBS] "+s)

# Get the installed pip modules
pips = subprocess.check_output("pip3 list", shell=True, stderr=subprocess.STDOUT)

# Required pip modules
libs = ["PyAutoGUI", "opencv-python", "playsound", "Pillow"]

# Checks if the modules are installed and if not installs them
for lib in libs:
    if lib in str(pips):
        log(lib+" exists, skipping")
    else:
        os.system("pip install "+lib)

import pyautogui
import cv2
from playsound import playsound

# Opens the website
webbrowser.open("https://workspace-zur3.ra.ubs.com/logon/choose-your-location/index.html", new=1, autoraise=True)

homeDIR = expanduser("~").replace("\\", "/")

ressources = "../ressources/"

# Select region by searching the country pic on the screen
cLoc = None
while(cLoc == None):
    cLoc  = pyautogui.locateOnScreen(ressources+"country.png", confidence=0.6)
    time.sleep(3)

# Clicks on switzerland
offset = (cLoc.width/7)
x, y = pyautogui.center(cLoc)
pyautogui.click(x+offset, y)

mLoc = None

# Clicks on the Mobile Login button
while(mLoc == None):
    mLoc = pyautogui.locateCenterOnScreen(ressources+"mobile.png", confidence=0.9)
    time.sleep(3)
    
pyautogui.click(mLoc)
pyautogui.move(200,0)

dLoc = None

# Plays sound the notify user and loops until it finds the download button for the remote computer
while(dLoc == None):
    playsound(ressources+"jingle.mp3")# sms
    time.sleep(15)
    dLoc  = pyautogui.locateCenterOnScreen(ressources+"download.png", confidence=0.9)

# Clicks on the download button
pyautogui.click(dLoc)


# Searches and open the remote pc file in the downloads folder
for file in os.listdir(homeDIR+"/Downloads"):
    if file.endswith(".ica"):
        os.system(file)
