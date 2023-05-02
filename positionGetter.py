from time import sleep
import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
print(screenWidth, screenHeight)


# while(1):
#     currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
#     # print(currentMouseX, currentMouseY)
def getPos():
    return pyautogui.position()

VALUES = [
    (0, 0, 0, 0), (255, 255, 255, 0), (255, 0 , 0, 0), ()
]
MATERIALS = [
    "sky", "cloud", "fog", "water", "hill", "mountain", "mud", "snow", "straw", "sea", "river", "flower", "bush", "grass", "forest", "dirt", "gravel", "sand", "stone", "stonewall"
]
def distance(rbgba):


# (1635, 170) (1700, 170) (1760, 170) (1825, 170) (1890, 170)
# (1635, 230) (1700, 230) (1760, 230) (1825, 230) (1890, 230)
# (1635, 290) (1700, 290) (1760, 290) (1825, 290) (1890, 290)
# (1635, 355) (1700, 355) (1760, 355) (1825, 355) (1890, 355)


# corner top 155 155
# corner bottom 717 715

# style = 1825 595
