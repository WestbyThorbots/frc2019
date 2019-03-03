#!/usr/bin/env python3
"""
Take the Stage
"""
from wpilib.command import Command

class TakeTheStage(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.elevator)
        self.height = 0

    def initialize(self):
        pass