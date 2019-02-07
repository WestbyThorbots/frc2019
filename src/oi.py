#!/usr/bin/python3
import wpilib
import hal
from wpilib.interfaces.generichid import GenericHID
from commands.punch import Punch
from commands.differentialdrive_with_xbox import DifferentialDriveWithXbox
from xboxbutton import XboxButton

class OI():
    def __init__(self, robot):
        self.robot = robot

        self.xbox0 = wpilib.XboxController
        self.button1 = XboxButton(self.xbox0, 1)
        self.button2 = XboxButton(self.xbox0, 2)
        self.button3 = XboxButton(self.xbox0, 3)
        self.button4 = XboxButton(self.xbox0, 4)
        self.button5 = XboxButton(self.xbox0, 5)
        self.button6 = XboxButton(self.xbox0, 6)
        self.button8 = XboxButton(self.xbox0, 8)

        self.button1.whenPressed(Punch(self.robot))
		
        #self.button2.whenPressed(new Grab())
		#self.button3.whenPressed(new DriveToDistance(0.11))
		#self.button4.whenPressed(new PlaceSoda())
        #self.button5.whenPressed(new PlaceSoda())
		#self.button6.whenPressed(new DriveToDistance(0.2))
		#self.button8.whenPressed(new Stow())