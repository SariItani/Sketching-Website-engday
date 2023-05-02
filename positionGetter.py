from time import sleep
import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
print(screenWidth, screenHeight)


while(1):
    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    # print(currentMouseX, currentMouseY)
def getPos():
    return pyautogui.position()


# sky 1635 170      mud 230
# cloud 1700 170    flower 290 
# hill 1760 170      stone 355
# mount 1825 170
# water 1890 170

# corner top 155 155
# corner bottom 717 715

# style = 1824 595