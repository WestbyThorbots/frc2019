#!/usr/bin/env python3
'''Manipulate various aspects of the Limelight camera.
'''

from wpilib.command import Subsystem
from networktables import NetworkTables

class LimeLight(Subsystem):
    '''Various objects and methods for interacting with the LimeLight camera.
    '''
    def __init__(self):
        '''Assign ports and save them for use in the move and stop methods.
        '''
        super().__init__()

        if NetworkTables.initialize(server='10.59.3.2'):
            print("NetworkTables initialized.")
        else:
            print("It would seem that NetworkTables is already initialized; proceeding")

        self.table = NetworkTables.getDefault().getTable('limelight')

    '''ledMode 	Sets limelight's LED state
    0: use the LED Mode set in the current pipeline
    1: force off
    2: force blink
    3: force on
    '''
    def LEDauto(self):
        if self.table.isConnected():
            self.table.putNumber('ledMode', 0)

    def LEDoff(self):
        if self.table.isConnected():
            self.table.putNumber('ledMode', 1)

    def LEDblink(self):
        if self.table.isConnected():
            self.table.putNumber('ledMode', 2)

    def LEDon(self):
        if self.table.isConnected():
            self.table.putNumber('ledMode', 3)
