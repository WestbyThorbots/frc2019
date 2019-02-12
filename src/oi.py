#!/usr/bin/python3
'''Operator Interface - one class: OI.
This is where the rubber meets the road: make the Xbox controller
do what we want it to do.
'''
from commands.punch import Punch
from commands.pull import Pull
from commands.open_claw import OpenClaw
from commands.close_claw import CloseClaw
from commands.move_arm_with_triggers import MoveArmWithTriggers
from commands.intake_cargo import IntakeCargo

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
        '''The Constructor - assign Xbox controller buttons to specific Commands.
        '''

        print("In OI:__init__")

        self.xbox0 = wpilib.XboxController(0)

        punch = JoystickButton(self.xbox0, XboxController.Button.kA)
        claw = JoystickButton(self.xbox0, XboxController.Button.kB)
        intake = JoystickButton(self.xbox0, XboxController.Button.kX)

        triggerbutton = TriggerButton(self.xbox0, .1)

        punch.whenPressed(Punch(robot))
        punch.whenReleased(Pull(robot))

        intake.whileHeld(IntakeCargo(robot))

        triggerbutton.whenPressed(MoveArmWithTriggers(robot))

        claw.toggleWhenPressed(OpenClaw(robot))

    def getXbox0(self):
        '''Return the first Xbox controller connected to the system.
        '''
        return self.xbox0
