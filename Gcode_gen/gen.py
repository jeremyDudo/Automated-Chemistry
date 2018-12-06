import numpy as np 
import datetime

class syringe():
    def __init__(self):
        """
        Note: not modular yet, setting constants for now!

        Components:

            resting: resting height such that the syringe does not knock over any vials when moveing [mm]
            in_tube; height to be considered 'inside a test tube' [mm]

            origin: [0,0,resting]

            max_volume: the maximum volume in the syringe [ml]
            dist_to_vol: conversion of how far the plunger needs to move /
                in order to pump 1 ml worth of liquid [mm/ml]

            max_speed: maximum speed that the syringe should move [mm/s]
            max_pump_rate: maximum pump rate without shearing liquid [mm/s]

            file: file to store the gcode
        """
        
        # strgtimestmp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

        self.resting = 100      # mm
        self.in_tube = 50       # mm

        self.pos = [0, 0, self.resting]

        self.max_volume = 1     # ml
        self.dist_to_vol = 57   # mm/ml 

        self.max_speed = 10     # temp, need to fix
        self.max_pump_rate = 10 # temp

        file = open("gcode.txt", "w") # constant override, everytime
        file.close() 


    def write_move(self, posI, posF):
        """
        Writes the gcode to a script

        Components:
            
        """
        print('Moving...')

        x_cor, y_cor = (posF[i] - posI[i] for i in range(2))

        # reset height before moving
        clear_height = "G0 Z"       # need to define where 'home' is on the Z axis
        
        # move to next location
        g_string = "G1 X{0} Y{1} E{2} F2000".format(x_cor, y_cor) # speed is set as const.

        # move into vial
        into_vial = "G1 Z{} F2000".format(self.in_tube)

        

        file = open("gcode.txt", "a")
        file.write(clear_height+ '\n')
        file.write(g_string+ "\n")
        file.write(into_vial+ "\n")

        file.close()

    def write_pump(self, pump):
        """
        pump: mL pushed[pos]/pulled[neg]
        """
        extrude = pump * self.dist_to_vol


    def read_script(self, locations):
        """
        uhhh
        """
        pass

    def wash(self):
        self.write_move(self.pos, self.pos_WashVial)

    def draw(self):
        pass

    def read_sheet(self, locations):
        """
        Assuming sheets to be locations of labeled vials
        'input'
        'wash'
        'output'
        """
        pass

test = syringe()
test.write_move([0,10,20], [2, 5, 20])
