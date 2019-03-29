#!/usr/bin/env python3
'''Punch the puncher.'''

from wpilib.command import Command

class InvertFront(Command):
    def __init__(self, robot):
        '''Save the robot object and pull in the puncher subsystem.'''
        super().__init__()

        self.robot = robot

    def initialize(self):
        '''Called just before this Command runs the first time.'''

    def execute(self):
        '''Called repeatedly when this Command is scheduled to run.'''
        self.robot.front *= -1

    def isFinished(self):
        '''Make this return true when this Command no longer needs to
        run execute().'''
        return True

    def end(self):
        '''Called once after isFinished returns true.'''
        pass

    def interrupted(self):
        '''Called when another Command which requires one or more of
        the same subsystems is scheduled to run.'''
        self.end()
