import pyautogui
from pynput import mouse
import time
import random

# GUI
import tkinter as tk
from tkinter import *

posx = 0
posy = 0

class MyException(Exception):pass

def on_click(x, y, button, pressed):
    global posx, posy
    posx = x
    posy = y
    raise MyException(button)
    
def mousepos():
    with mouse.Listener(on_click=on_click) as listener:
        try:
            listener.join()
        except MyException as e:
            pass

def setMousePos(id):
    global posx, posy
    if id == 1:
        mousepos()
        click_1_var_posx.insert(0, posx)
        click_1_var_posy.insert(0, posy)
    if id == 2:
        mousepos()
        click_2_var_posx.insert(0, posx)
        click_2_var_posy.insert(0, posy)
    if id == 3:
        mousepos()
        click_3_var_posx.insert(0, posx)
        click_3_var_posy.insert(0, posy)
    if id == 4:
        mousepos()
        click_4_var_posx.insert(0, posx)
        click_4_var_posy.insert(0, posy)
    if id == 5:
        mousepos()
        click_5_var_posx.insert(0, posx)
        click_5_var_posy.insert(0, posy)
        

def startClicker():
    while True:
        
        #get data from inputs + random
        c1x = int(click_1_var_posx.get()) + random.randint(-5, 5)
        c1y = int(click_1_var_posy.get()) + random.randint(-5, 5)
        c2x = int(click_2_var_posx.get()) + random.randint(-5, 5)
        c2y = int(click_2_var_posy.get()) + random.randint(-5, 5)
        c3x = int(click_3_var_posx.get()) + random.randint(-5, 5)
        c3y = int(click_3_var_posy.get()) + random.randint(-5, 5)
        c4x = int(click_4_var_posx.get()) + random.randint(-5, 5)
        c4y = int(click_4_var_posy.get()) + random.randint(-5, 5)
        c5x = int(click_5_var_posx.get()) + random.randint(-5, 5)
        c5y = int(click_5_var_posy.get()) + random.randint(-5, 5)
        runTime = int(runTime_var.get()) + random.randint(0, 5)
        
        #initial delay
        time.sleep(int(delay_var.get())+ random.randint(0, 2))
        
        #click 1
        if(c1x and c1y): 
            pyautogui.click(c1x, c1y)
            time.sleep(2+random.randint(0, 3)) 
        
        #click 2    
        if(c2x and c2y):
            pyautogui.click(c2x, c2y)
            time.sleep(2+random.randint(0, 3))
        
        #click 3       
        if(c3x and c3y):
            pyautogui.click(c3x, c3y)
            time.sleep(2+random.randint(0, 3))
            
        #click 4
        if(c4x and c4y):
            pyautogui.click(c4x, c4y)
            time.sleep(2+random.randint(0, 3)) 

        #click 5
        if(c5x and c5y):
            pyautogui.click(c5x, c5y)
            time.sleep(2+random.randint(0, 3)) 
        
        #runtime delay        
        time.sleep(runTime) 
  
  
#GUI      
window = tk.Tk()
window.eval('tk::PlaceWindow . center')
window.title("SW Clicker by Bruno Ferreira")
window.minsize(500, 200)
window.configure(bg="black")

click_1_Label = Label(window, text="Click 1", bg="black", fg="white")
click_1_Label.grid(column=0, row=0, sticky=W, padx=5)
click_1_var_posx = StringVar()
click_1_var_posx = Entry(window, width=10,textvariable=click_1_var_posx, bg="black", fg="white")
click_1_var_posx.grid(column=2, row=0, sticky=W, padx=5, columnspan=4)
click_1_var_posy = StringVar()
click_1_var_posy = Entry(window, width=10,textvariable=click_1_var_posy, bg="black", fg="white")
click_1_var_posy.grid(column=6, row=0, sticky=W, padx=5, columnspan=4)
button_1 = Button(window, text="Set", command=lambda: setMousePos(1))
button_1.grid(column=10, row=0, sticky=W, padx=5, columnspan=4)

click_2_Label = Label(window, text="Click 2 ", bg="black", fg="white")
click_2_Label.grid(column=0, row=1, sticky=W, padx=5)
click_2_var_posx = StringVar()
click_2_var_posx = Entry(window, width=10,textvariable=click_2_var_posx, bg="black", fg="white")
click_2_var_posx.grid(column=2, row=1, sticky=W, padx=5, columnspan=4)
click_2_var_posy = StringVar()
click_2_var_posy = Entry(window, width=10,textvariable=click_2_var_posy, bg="black", fg="white")
click_2_var_posy.grid(column=6, row=1, sticky=W, padx=5, columnspan=4)
button_2 = Button(window, text="Set", command=lambda: setMousePos(2))
button_2.grid(column=10, row=1, sticky=W, padx=5, columnspan=4)

click_3_Label = Label(window, text="Click 3 ", bg="black", fg="white")
click_3_Label.grid(column=0, row=2, sticky=W, padx=5)
click_3_var_posx = StringVar()
click_3_var_posx = Entry(window, width=10,textvariable=click_3_var_posx, bg="black", fg="white")
click_3_var_posx.grid(column=2, row=2, sticky=W, padx=5, columnspan=4)
click_3_var_posy = StringVar()
click_3_var_posy = Entry(window, width=10,textvariable=click_3_var_posy, bg="black", fg="white")
click_3_var_posy.grid(column=6, row=2, sticky=W, padx=5, columnspan=4)
button_3 = Button(window, text="Set", command=lambda: setMousePos(3))
button_3.grid(column=10, row=2, sticky=W, padx=5, columnspan=4)

click_4_Label = Label(window, text="Click 4 ", bg="black", fg="white")
click_4_Label.grid(column=0, row=3, sticky=W, padx=5)
click_4_var_posx = StringVar()
click_4_var_posx = Entry(window, width=10,textvariable=click_4_var_posx, bg="black", fg="white")
click_4_var_posx.grid(column=2, row=3, sticky=W, padx=5, columnspan=4)
click_4_var_posy = StringVar()
click_4_var_posy = Entry(window, width=10,textvariable=click_4_var_posy, bg="black", fg="white")
click_4_var_posy.grid(column=6, row=3, sticky=W, padx=5, columnspan=4)
button_4 = Button(window, text="Set", command=lambda: setMousePos(4))
button_4.grid(column=10, row=3, sticky=W, padx=5, columnspan=4)

click_5_Label = Label(window, text="Click 5 ", bg="black", fg="white")
click_5_Label.grid(column=0, row=4, sticky=W, padx=5)
click_5_var_posx = StringVar()
click_5_var_posx = Entry(window, width=10,textvariable=click_5_var_posx, bg="black", fg="white")
click_5_var_posx.grid(column=2, row=4, sticky=W, padx=5, columnspan=4)
click_5_var_posy = StringVar()
click_5_var_posy = Entry(window, width=10,textvariable=click_5_var_posy, bg="black", fg="white")
click_5_var_posy.grid(column=6, row=4, sticky=W, padx=5, columnspan=4)
button_5 = Button(window, text="Set", command=lambda: setMousePos(5))
button_5.grid(column=10, row=4, sticky=W, padx=5, columnspan=4)

delay_Label = Label(window, text="Start delay (seconds) ", bg="black", fg="white")
delay_Label.grid(column=0, row=5, sticky=W, padx=5)
delay_var = StringVar()
delay_var = Entry(window, width=10,textvariable=delay_var, bg="black", fg="white")
delay_var.grid(column=2, row=5, sticky=W, padx=5, columnspan=4)
delay_var.insert(0, 5)

runTime_Label = Label(window, text="Max run time (seconds) ", bg="black", fg="white")
runTime_Label.grid(column=0, row=8, sticky=W, padx=5)
runTime_var = StringVar()
runTime_var = Entry(window, width=10,textvariable=runTime_var, bg="black", fg="white")
runTime_var.grid(column=2, row=8, sticky=W, padx=5, columnspan=4)
runTime_var.insert(0, 55)

button_start = Button(window, text="Start", command=startClicker)
button_start.grid(column=6, row=8, sticky=W, padx=5, columnspan=8)
    
window.mainloop()