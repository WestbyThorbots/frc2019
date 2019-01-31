#!/usr/bin/python3
"""
This lifts the robot
"""
from wpilib.command import Command

class LiftFront(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.elevator)

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
        self.robot.elevator.Stop()

    def interrupted(self):
        self.end()
