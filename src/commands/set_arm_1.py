#!/usr/bin/python3
"""
This program is designed to alter the height of the arm, primarlly to one of 
the 3 stages of the rocket.
"""
import wpilib
from wpilib.command import Command

class SetArm1(Command):
    def __init__(self, robot):
        super().__init__()
        
        self.robot = robot
        self.requires(self.robot.arm)
        self.angle = wpilib.Encoder

    def initialize(self):
        """ TODO: fill in the missing pieces for initialization. """
        if (self.angle < 30):
            self.robot.arm.RaiseArm()
        elif (self.angle > 30):
            self.robot.arm.LowerArm()
        else:
            self.robot.arm.StopArm()

    def execute(self, controller):
        pass

    def isFinished(self):
        """ Return "True" when we are done with this command. """
        if (self.angle == 30):
            return True

    def end(self):
        if (self.angle == 30):
            self.robot.arm.StopArm()

    def interrupted(self):
        self.end()

        """TODO: Get someone who actually knows what they are doing on this program."""
        