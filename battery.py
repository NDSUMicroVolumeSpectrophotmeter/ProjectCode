import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import ttk


normFont = ("Verdana", 10)

def popUpMsg(msg):
    popup = tk.Tk()

    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=normFont)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destory)
    B1.pack()
    popup.mainloop90

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while(True):
    if not(GPIO.input(37)):
        msg = "The Battery Voltage is low Please Recharge"
        popUpMsg(msg)