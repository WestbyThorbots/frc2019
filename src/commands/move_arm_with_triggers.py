#!/usr/bin/python3
import wpilib
from wpilib.command import Command

class MoveArmWithTriggers(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.arm)

    def initialize(self):
        #Called just before this Command runs the first time
        self.robot.arm.move()
        print ("arm initialize")

    def execute(self):
        #Called repeatedly when this Command is scheduled to run
        self.robot.arm.move()
        print ("arm execute")

    def isFinished(self):
        #Make this return true when this Command no longer needs to run execute()
        print ("arm isFinished")
        return self.isTimedOut()

    def end(self):
        #Called once after isFinished returns true
        print ("arm end")

    def interrupted(self):
        '''Called when another Command which requires one or more of the same
        subsystems is scheduled to run
        '''
        print ("arm interrupted")
        self.end()
