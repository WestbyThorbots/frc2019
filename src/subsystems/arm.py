#!/usr/bin/env python3
'''Raise and lower the robot's arm.'''

import wpilib
from wpilib.command import Subsystem
from commands.move_arm_with_triggers import MoveArmWithTriggers
from wpilib import XboxController
from wpilib.interfaces.generichid import GenericHID

class Arm(Subsystem):
    """Raise and lower the robot's arm."""
    def __init__(self):
        """Assign ports and save them for use in the move and stop methods."""
        super().__init__()

        self.xbox0 = XboxController(0)
        self.arm = wpilib.VictorSP(2)

    def move(self):
        """Move the arm according to the left and right Xbox
        controller triggers."""
        self.arm.set(self.xbox0.getTriggerAxis(GenericHID.Hand.kRight) -
                     self.xbox0.getTriggerAxis(GenericHID.Hand.kLeft))

    def stop(self):
        """Stop the arm."""
        self.arm.set(0.0)
        #TODO: Change 0.0 to a value that holds the arm at its current value so it doesn't fall.
