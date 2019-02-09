#!/usr/bin/python3

#arm.py controls how the arm moves up and down.

import wpilib
from wpilib.command import Subsystem
from commands.move_arm_with_triggers import MoveArmWithTriggers
from wpilib import XboxController
from wpilib.interfaces.generichid import GenericHID

class Arm(Subsystem):

    def __init__(self):
        super().__init__()

        self.xbox0 = XboxController(0)
        self.arm = wpilib.VictorSP(2)

    def move(self):
        self.arm.set(self.xbox0.getTriggerAxis(GenericHID.Hand.kRight) - self.xbox0.getTriggerAxis(GenericHID.Hand.kLeft))
        
    def stop(self):
        self.arm.set(0.0)
        #TODO: Change 0.0 to a value that holds the arm at its current value so it doesn't fall.