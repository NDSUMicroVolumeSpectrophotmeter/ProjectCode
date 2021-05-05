# Micro-Volume Spectrophotometer
#SD-2014
#Luke Halverson, Dylan Ditlevson, Nate Howe, Thomas Smallarz, Ryan Peters
import tkinter as tk


#This is the function for the popup message that appears before trying to run the tests on the sample
def popupmsg(msg):
	popup = tk.Tk()
	popup.wm_title("!")
	label = tk.Label(popup, text=msg)
	label.pack(side="top", fill="x", pady=10)
	ok_button = tk.Button(popup, text="Okay", command = popup.destroy)
	ok_button.pack()
	popup.mainloop()


#These two functions are the commands that the button clicks give out. They collect the value for e
#and then they output the concentration. An error is thrown if e is invalid
def submit450():
    try:
        e = float(entry.get())
        concentration450 = test450(e)
        print("You have chosen to test for 450nm")
        print("The concentration is " + str(concentration450) + " Moles liter")
    except Exception as e:
        print(e)

def submit500():
    try:
        e = float(entry.get())
        concentration500 = test500(e)
        print("You have chosen to test for 500nm")
        print("The concentration is " +str(concentration500)+" Moles/liter")
    except Exception as e:
        print(e)
        print("Please enter a proper value for e")

#This section of code is the actual GUI part that you enter the value for e and which test you want.
window = tk.Tk()
label = tk.Label(text="Enter value for e and select test type:")
entry = tk.Entry()
label.pack()
entry.pack()
button = tk.Button(text = "450nm", command = submit450, width = 35, height = 40)
button.pack(side=tk.LEFT)
button2 = tk.Button(text = "500nm", command = submit500, width = 35, height =40)
button2.pack(side=tk.LEFT)
window.mainloop()
