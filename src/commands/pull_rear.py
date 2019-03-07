#!/usr/bin/env python3
'''Pull something.'''

from wpilib.command import Command

class PullRear(Command):
    '''Pull something.'''
    def __init__(self, robot):
        '''Save the robot object and pull in the puncher subsystem.'''
        super().__init__()

        self.robot = robot
        self.requires(self.robot.rear_puncher)

    def initialize(self):
        '''Called just before this Command runs the first time
        '''
        self.robot.rear_puncher.close()

    def execute(self):
        '''Called repeatedly when this Command is scheduled to run
        '''
        self.robot.rear_puncher.close()

    def isFinished(self):
        '''Make this return true when this Command no longer needs to
        run execute()'''
        return self.isTimedOut()

    def end(self):
        '''Called once after isFinished returns true
        '''
        self.robot.rear_puncher.close()

    def interrupted(self):
        '''Called when another Command which requires one or more of
        the same subsystems is scheduled to run.'''
        self.end()
