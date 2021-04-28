# Micro-Volume Spectrophotometer
#SD-2014
#Luke Halverson, Dylan Ditlevson, Nate Howe, Thomas Smallarz, Ryan Peters

import tkinter as tk
def submit():
    try:
        e = float(entry.get())
        #This is where the test would be run with e as the Molar Absorbtivity.
        print("You have chosen to test for 500nm")
    except:
        print("Please enter a proper value for e")

def submit2():
    try:
        e = float(entry.get())
        #This is where the test would be run with e as the Molar Absorbtivity.
        print("You have chosen to test for 500nm")
    except:
        print("Please enter a proper value for e")

window = tk.Tk()
label = tk.Label(text="Enter value for e and select test type:")
entry = tk.Entry()
label.pack()
entry.pack()
button = tk.Button(text = "Solvent", command = submit, width = 35, height = 40)
button.pack(side=tk.LEFT)
button2 = tk.Button(text = "Sample", command = submit2, width = 35, height =40)
button2.pack(side=tk.LEFT)
window.mainloop()