#!/usr/bin/env python3
'''Move the bot in a linear direction. But not sideways. Or any direction besides forward or backward.'''

from wpilib.command import Command
from wpilib import XboxController
from wpilib.interfaces.generichid import GenericHID

class DriveStraight(Command):
    """move the robot forward or backwards"""
    def __init__(self, robot, distance, speed):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.drivetrain)
        self.distance = distance
        self.speed = speed

    def initialize(self):
        #Called just before this Command runs the first time
        self.robot.drivetrain.reset()
        print ("gyro is reset in drive_straight initialize")

    def execute(self):
        #Called repeatedly when this Command is scheduled to run
        if self.robot.drivetrain.getDistance() < self.distance:
            self.robot.drivetrain.driveStraight(self.speed)
        else:
            self.robot.drivetrain.driveStraight(0)

    def isFinished(self):
        #Make this return true when this Command no longer needs to run execute()
        if self.robot.drivetrain.getDistance() >= self.distance:
            return True

    def end(self):
        #Called once after isFinished returns true
        self.robot.drivetrain.driveStraight(0)

    def interrupted(self):
        '''Called when another Command which requires one or more of the same
        subsystems is scheduled to run
        '''
        self.end()

