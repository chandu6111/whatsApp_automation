import webbrowser
import time
import pyautogui as gui
interval=1
position=1138,338
print("enter ph no:")
numbers=[i for i in input().split()]
message=input("Enter message")
for j in numbers:
    url="https://wa.me/{}?text={}".format(j,message)
    webbrowser.open(url)
    time.sleep(3)
    gui.click(position)
    time.sleep(3)
    gui.press('enter')
    time.sleep(interval)
