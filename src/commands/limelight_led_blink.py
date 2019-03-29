#!/usr/bin/env python3
'''Flash the Limelight LEDs.
'''

from wpilib.command import Command

class LimeLightLEDblink(Command):
    '''Blind 'em with strobe lights!
    '''

    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.limelight)

    def initialize(self):
        pass

    def execute(self):
        self.robot.limelight.LEDblink()

    def isFinished(self):
        return self.isTimedOut()

    def end(self):
        pass

    def interrupted(self):
        self.end()
