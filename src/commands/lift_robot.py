#!/usr/bin/env python3
'''Lift the robot.'''

from wpilib.command import Command

class LiftRobot(Command):
    '''Lift the robot.'''
    def __init__(self, robot):
        '''Save the robot object and pull in the elevator subsystem.'''
        super().__init__()

        self.robot = robot
        self.requires(self.robot.elevator)
