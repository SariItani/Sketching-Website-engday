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
    (121, 231, 245, 0), (97, 126, 123, 0), (59, 222, 138, 0), (138, 122, 92, 0), (172, 194, 254, 0), (147, 53, 13, 0), (74, 198, 178, 0), (135, 216, 255, 0), (131, 206, 207, 0), (141, 171, 251, 0), (134, 0, 142, 0), (70, 202, 0, 0), (125, 231, 99, 0), (88, 115, 43, 0), (144, 212, 50, 0), (161, 83, 52 ,0), (152, 148, 0 ,0), (131, 84, 84, 0), (117, 74, 26, 0), (171, 174, 119, 0)
]
MATERIALS = [
    "Sky", "Cloud", "Hill", "Mountain", "Water", "Mud", "Fog", "Snow", "Sea", "River", "Flower", "Grass", "Straw", "Bush", "Forest", "Stone", "Sand", "Gravel", "Dirt", "Stone Wall"
]
# def distance(rbgba):


# (1635, 170) (1700, 170) (1760, 170) (1825, 170) (1890, 170)
# (1635, 230) (1700, 230) (1760, 230) (1825, 230) (1890, 230)
# (1635, 290) (1700, 290) (1760, 290) (1825, 290) (1890, 290)
# (1635, 355) (1700, 355) (1760, 355) (1825, 355) (1890, 355)


# corner top 155 155
# corner bottom 717 715

# style = 1825 595
