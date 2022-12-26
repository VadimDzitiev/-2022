import pyautogui

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    r = Rectangle("синего", 3, 2)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    print(r)
    print(c)
    print(s)
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'file name.png')
if __name__ == "__main__":
    main()