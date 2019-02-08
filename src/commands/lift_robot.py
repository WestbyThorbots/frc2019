#!/usr/bin/env python3

from wpilib.command import Command

class LiftRobot(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
