# Micro-Volume Spectrophotometer
#SD-2014
#Luke Halverson, Dylan Ditlevson, Nate Howe, Thomas Smallarz, Ryan Peters
#Rev 1
#Last Update: 4/5/2021

#Imports used in this concetration test
import time
import board
import busio
import sys
import math
from gpiozero import LED
from signal import pause

from adafruit_as726x import AS726x_I2C

#this function does the 450nm test
def test450(e):
    averageSolvent = 0 #averaging the test with 5 data points

    #waits for the user to input just the solvent
    while(True):
        solv = input("Solvent: y/n\n")
        if(solv == 'y'):
            break

    #takes 5 data points of the solvent at the 450nm mark
    for i in range(5):
        print("testing solvent " + str(i))                  #printing what test it is doing for debuging purposes
        averageSolvent += sensor.violet                     #this takes the current light sensor reading at 450nm and adds it to an average accumulator
        print(sensor.violet)                                #also printing what the close to what the sensor value is for debuging

    averageSolvent = averageSolvent/5                       #dividing by 5 to get the average value

    print("average solvent: " + str(averageSolvent))        #printing the average value

    averageSample = 0                                       #allowing the user to switch to the sample berfore running the test
    while(True):
        solv = input("Sample: y/n\n")
        if(solv == 'y'):
            break

                                                            #taking the 5 data points for the sample
    for i in range(5):
        print("testing sample " + str(i))                   #debuging print
        averageSample += sensor.violet                      #accumulating the sample light data
        print(sensor.violet)                                #debuging print

    averageSample = averageSample/5                         #dividing by 5 to get average

    print("\naveragesample: " + str(averageSample))         

    absorbance = -1 * math.log10(averageSample/averageSolvent) #absorbance is -log10(sample/solvent)

    print("\nabsorbanceabsorbance: " + str(absorbance))     #printing the calulated absorbance

    concentraction = (e * 10e-6) / absorbance               #using beer's law A=ecl, e is the molar absorptivity coefficent, 10e-6 is 10uL, absorbance was calulated above giving us concentration
    return concentraction                                   #returning the concentration

#doing the same as the 450test but using the blue sensor follows above exactly 
def test500(e):
    averageSolvent = 0

    while(True):
        solv = input("Solvent: y/n\n")
        if(solv == 'y'):
            break

    for i in range(5):
        print("testing solvent " + str(i))
        averageSolvent += sensor.blue
        print(sensor.blue)

    averageSolvent = averageSolvent/5

    print("averageSolvent: " + str(averageSolvent))

    averageSample = 0
    while(True):
        solv = input("Sample: y/n\n")
        if(solv == 'y'):
            break

    for i in range(5):
        print("testing sample " + str(i))
        averageSample += sensor.blue
        print(sensor.blue)

    averageSample = averageSample/5

    print("\naveragesample: " + str(averageSample))

    absorbance = -1 * math.log10(averageSample/averageSolvent)

    print("\nabsorbanceabsorbance: " + str(absorbance))

    concentraction = (e * 10e-6) / absorbance
    return concentraction


#initializing light sensor 
i2c = busio.I2C(board.SCL, board.SDA)
sensor = AS726x_I2C(i2c)

#main code run here
while True:

    print("Micro-Volume Spectrophotometer\n")   #introduction splash

    #this sets the LED to their GPIO pins
    LED1 = LED(22)
    LED2 = LED(27)
    LED3 = LED(5)
    LED4 = LED(6)

    #turning all leds on will change to an individual led when LEDs are finalized
    LED1.on()
    LED2.on()
    LED3.on()
    LED4.on()

    #getting the users info for the test
    #Here's where the GUI stuff will go.
    print("Would you like to run a test at 450nm? y/n")                                 #asking about 450nm test
    in450 = input()                                                                     #getting users input if y running 450 test if not ask about 500nm
    if(in450 == "y"):
        while(True):
            print("What is the Molar Absorptivity of the Sample?")                      #getting the Molar absorbitivity will change once I know these values for sure
            e = input()                                                                 #taking their input and storing in e
            try:
                molarAbsorptivity = float(e)                                            #trying casting input to float otherwise re asking for coefficent
                concentration450 = test450(molarAbsorptivity)                           #running 450nm test
                print("The concentraction at 450nm is: " + str(concentration450))       #printing concentration
                break
            except:
                print("Please input a valid Molar Absorbtivity") 

    #running the same as above but for 500nm 
    print("Would you like to run a test at 500nm? y/n")
    in500 = input()
    if(in500 == "y"):
        while(True):
            print("What is the Molar Absorptivity of the Sample?")
            e = input()
            try:
                molarAbsorptivity = float(e)
                concentration500 = test500(molarAbsorptivity)
                print("The concentraction at 450nm is: " + str(concentration500))
                break
            except:
                print("Please input a valid Molar Absorbtivity")

    time.sleep(1)