#!/usr/bin/env python3
'''turn the robot'''

from wpilib.command import Command
from wpilib import XboxController
from wpilib.interfaces.generichid import GenericHID

class Turn(Command):
    """turn the robot"""
    def __init__(self, robot, angle, speed):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.drivetrain)
        self.angle = angle
        self.speed = speed

    def initialize(self):
        #Called just before this Command runs the first time
        self.robot.drivetrain.reset()
        #self.initial_heading = self.robot.drivetrain.getHeading()
        #self.target_heading = self.initial_heading + self.angle

    def execute(self):
        #Called repeatedly when this Command is scheduled to run
        self.robot.drivetrain.turn(self.angle, self.speed)

    def isFinished(self):
        #Make this return true when this Command no longer needs to run execute()
        return self.robot.drivetrain.turn_complete


    def end(self):
        #Called once after isFinished returns true
        self.robot.drivetrain.driveManual(0, 0)

    def interrupted(self):
        '''Called when another Command which requires one or more of the same
        subsystems is scheduled to run
        '''
        self.end()
