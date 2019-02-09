#!/usr/bin/python3
import wpilib
from wpilib.command import Command

class Pull(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.puncher)

    def initialize(self):
        '''Called just before this Command runs the first time
        '''
        self.robot.puncher.close()
        print("Pull:initialize()")

    def execute(self):
        '''Called repeatedly when this Command is scheduled to run
        '''
        self.robot.puncher.close()
        print("Pull:execute")

    def isFinished(self):
        '''Make this return true when this Command no longer needs to run execute()
        '''
        print("Pull:isFinished")
        return self.isTimedOut()

    def end(self):
        '''Called once after isFinished returns true
        '''
        self.robot.puncher.close()
        print("Pull:end")

    def interrupted(self):
        '''Called when another Command which requires one or more of the same
        subsystems is scheduled to run
        '''
        self.end()