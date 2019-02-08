#!/usr/bin/python3
'''Operator Interface - one class: OI.
'''
from commands.punch import Punch
#from commands.differentialdrive_with_xbox import DifferentialDriveWithXbox
from wpilib.buttons import JoystickButton
from wpilib import XboxController
import wpilib

class OI:
    '''Operator Interface - all button assignments and other human interface elements
    '''

    def __init__(self, robot):
        print("In OI:__init__")

        self.xbox0 = wpilib.XboxController(0)

        punch = JoystickButton(self.xbox0, XboxController.Button.kA)

        punch.whenPressed(Punch(robot))
        #self.button2.whenPressed(new Grab())
		#self.button3.whenPressed(new DriveToDistance(0.11))
		#self.button4.whenPressed(new PlaceSoda())
        #self.button5.whenPressed(new PlaceSoda())
		#self.button6.whenPressed(new DriveToDistance(0.2))
		#self.button8.whenPressed(new Stow())

    def getXbox0(self):
        return self.xbox0
