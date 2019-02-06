#!/usr/bin/python3
"""
This program is designed to alter the height of the arm, primarlly to one of 
the 3 stages of the rocket.
"""

from wpilib.command import Command

class MoveArm (Command):
    def __init__(self, robot):
        super().__init__()
        
        self.robot = robot
        self.requires(self.robot.arm)

    def initialize(self):
        """ TODO: fill in the missing pieces for initialization. """


    def execute(self, controller):
        """ TODO: make the lift actually do something. """
        value = self.robot.oi.getRightTrigger() - self.robot.oi.getLeftTrigger()
        print ("In MoveArm value is " + "%2.5f" % value)
        self.robot.arm.MoveArm(value)
        

    def isFinished(self):
        """ Return "True" when we are done with this command. """
        return self.isTimedOut()

    def end(self):
        self.robot.arm.StopArm()

    def interrupted(self):
        self.end()

        """TODO: Get someone who actually knows what they are doing on this program."""
        