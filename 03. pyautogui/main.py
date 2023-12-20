from tkinter import *
import pyautogui

window = Tk()
window.title("Screen shot")

def handle_click():
    screenshot = pyautogui.screenshot()
    screenshot.save('screen.png')

button = Button(window, text="Example screen shot", command=handle_click)
button.grid(row = 50, column = 50)

window.mainloop()