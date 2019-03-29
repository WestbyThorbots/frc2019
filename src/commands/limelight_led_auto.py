#!/usr/bin/env python3
'''Set the Limelight LEDs to whatever the pipeline wants.
'''

from wpilib.command import Command

class LimeLightLEDauto(Command):
    '''Auto LEDs.
    '''

    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.limelight)

    def initialize(self):
        pass

    def execute(self):
        self.robot.limelight.LEDauto()

    def isFinished(self):
        return self.isTimedOut()

    def end(self):
        pass

    def interrupted(self):
        self.end()
