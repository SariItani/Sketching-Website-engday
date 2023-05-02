from time import sleep
import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.


while(1):
    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    print(currentMouseX, currentMouseY)

