#!/usr/bin/python3
'''Operator Interface - one class: OI.
'''
from commands.punch import Punch
from commands.pull import Pull
from commands.open_claw import OpenClaw
from commands.close_claw import CloseClaw
from commands.move_arm_with_triggers import MoveArmWithTriggers

#from commands.differentialdrive_with_xbox import DifferentialDriveWithXbox
from wpilib.buttons import JoystickButton
from wpilib import XboxController
import wpilib
from wpilib.interfaces.generichid import GenericHID
from wpilib import Timer
from thresholds import TriggerButton

class OI:
    '''Operator Interface - all button assignments and other human interface elements
    '''

    def __init__(self, robot):
        print("In OI:__init__")

        self.xbox0 = wpilib.XboxController(0)

        punch = JoystickButton(self.xbox0, XboxController.Button.kA)
        claw = JoystickButton(self.xbox0, XboxController.Button.kB)

        triggerbutton = TriggerButton(self.xbox0, .1)

        punch.whenPressed(Punch(robot))
        punch.whenReleased(Pull(robot))

        triggerbutton.whenPressed(MoveArmWithTriggers(robot))

        claw.toggleWhenPressed(OpenClaw(robot))

        #self.button2.whenPressed(new Grab())
		#self.button3.whenPressed(new DriveToDistance(0.11))
		#self.button4.whenPressed(new PlaceSoda())
        #self.button5.whenPressed(new PlaceSoda())
		#self.button6.whenPressed(new DriveToDistance(0.2))
		#self.button8.whenPressed(new Stow())

    def getXbox0(self):
        return self.xbox0
