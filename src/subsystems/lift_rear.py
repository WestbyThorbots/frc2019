#!/usr/bin/env python3
'''Lifts the back of the robot.'''

from wpilib.command import Command

class LiftRear(Command):
    '''Punch the puncher.'''
    def __init__(self, robot):
        '''Save the robot object and pull in the puncher subsystem.'''
        super().__init__()

        self.robot = robot
        self.requires(self.robot.lift.py)

    def initialize(self):
        '''Called just before this Command runs the first time.'''
        print("Punch:initialize()")

    def execute(self):
        '''Called repeatedly when this Command is scheduled to run.'''
        print("Punch:execute")
        self.robot.lift.liftRear()

    def isFinished(self):
        '''Make this return true when this Command no longer needs to
        run execute().'''
        print("Punch:isFinished")
        return True

    def end(self):
        '''Called once after isFinished returns true.'''
        print("Punch:end")
        self.robot.lift.lowerRear()

    def interrupted(self):
        '''Called when another Command which requires one or more of
        the same subsystems is scheduled to run.'''
        print("Punch:interrupted")
        self.end()
