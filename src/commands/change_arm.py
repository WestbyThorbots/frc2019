#!/usr/bin/python3
"""
This program is designed to alter the height of the arm, primarlly to one of 
the 3 stages of the rocket.
"""

from wpilib.command import Command

class LiftArm (Command):
     def __init__(self, robot):
        super().__init__()

            self.robot = robot
            self.requires(self.robot.arm)

      def initialize(self):
        """ TODO: fill in the missing pieces for initialization. """
        pass

    def execute(self):
        """ TODO: make the lift actually do something. """
        pass

    def isFinished(self):
        """ Return "True" when we are done with this command. """
        return self.isTimedOut()

    def end(self):
        self.robot.arm.Stop()

    def interrupted(self):
        self.end()

        """TODO: Get someone who actually knows what they are doing on this program."""
        