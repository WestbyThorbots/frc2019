#!/usr/bin/env python3
'''Turn the Limelight LEDs on.
'''

from wpilib.command import Command

class LimeLightLEDon(Command):
    '''Turn things green.
    '''

    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.limelight)

    def initialize(self):
        pass

    def execute(self):
        self.robot.limelight.LEDon()

    def isFinished(self):
        return self.isTimedOut()

    def end(self):
        pass

    def interrupted(self):
        self.end()
