# Add your Python code here. E.g.
from microbit import *
#water_level = pin1.read_analog

while True:
    if pin1.read_analog() > 520:
        pin0.write_digital(1)
    if pin1.read_analog() > 590: 
        pin0.write_digital(1)
    if pin1.read_analog() > 610:   
        pin0.write_digital(1)
    pin0.write_digital(0)    
        